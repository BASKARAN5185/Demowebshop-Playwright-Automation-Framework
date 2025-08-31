import pytest
import re
import webbrowser
import platform
import time
import allure
import subprocess
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

# 📁 Directory to store screenshots or artifacts
ARTIFACTS_DIR = Path("test-artifacts")
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

# 🧼 Sanitize test names for filenames
def sanitize_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*@\[\]\s]', "_", name)

# ✅ Shared Playwright instance
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

# ✅ Launch browser once per session
@pytest.fixture(scope="session")
def browser(playwright_instance) -> Browser:
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=100)
    yield browser
    browser.close()

# ✅ Shared browser context
@pytest.fixture(scope="session")
def context(browser) -> BrowserContext:
    context = browser.new_context(viewport={"width": 1920, "height": 1080}, ignore_https_errors=True)
    yield context
    context.close()

# ✅ Shared page instance
@pytest.fixture(scope="session")
def page(context) -> Page:
    page = context.new_page()
    yield page
    page.close()

# ✅ Login Page Object fixture
@pytest.fixture
def login_page(page: Page):
    from pages.login_page import Loginpage
    login = Loginpage(page)
    login.navigate("https://demowebshop.tricentis.com/login")
    yield login

# ✅ Capture screenshot and attach to Allure on failure
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if isinstance(page, Page):
            test_name = sanitize_filename(item.nodeid)
            screenshot_path = ARTIFACTS_DIR / f"{test_name}_failed.png"

            try:
                page.wait_for_load_state("networkidle", timeout=10000)
                page.screenshot(path=str(screenshot_path), timeout=10000)
                print(f"\n📸 Screenshot captured on failure: {screenshot_path}")

                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name="Failure Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
            except Exception as e:
                print(f"❌ Failed to capture screenshot: {e}")

# ✅ Clean old report folder at start of test session
def pytest_sessionstart(session):
    print("\n🧹 Cleaning old Allure report directory...")

    report_dir = Path("allure-report")
    if report_dir.exists():
        shutil.rmtree(report_dir)
        print(f"🗑️ Deleted allure-report")
    report_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 Created allure-report")

# ✅ Generate and open Allure report automatically after session
def pytest_sessionfinish(session, exitstatus):
    print("\n📊 Generating Allure report...")

    results_dir = Path("allure-results")
    report_dir = Path("allure-report")

    if shutil.which("allure") is None:
        print("❌ Allure CLI not found. Please install Allure and add it to your PATH.")
        return

    try:
        # Generate Allure report
        subprocess.run(["allure", "generate", str(results_dir), "-o", str(report_dir), "--clean"], check=True)
        print("✅ Allure report generated successfully.")

        # Open the report
        if platform.system() == "Windows":
            subprocess.Popen("allure open allure-report", shell=True)
        else:
            subprocess.Popen(["allure", "open", "allure-report"])

        print("🌐 Attempting to open Allure report in browser...")

        time.sleep(3)

        report_index = report_dir / "index.html"
        if report_index.exists():
            url = report_index.resolve().as_uri()
            webbrowser.open(url)
            print(f"🔗 Fallback opened at: {url}")
        else:
            print("⚠️ Fallback index.html not found.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Allure generate command failed: {e}")
    except Exception as e:
        print(f"❌ Error during report generation/opening: {e}")
