import pytest
import re
import allure
from pathlib import Path
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

# Directory to store screenshots or artifacts
ARTIFACTS_DIR = Path("test-artifacts")
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

# Helper to sanitize filenames for artifacts
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

# ✅ Shared browser context (session-wide)
@pytest.fixture(scope="session")
def context(browser) -> BrowserContext:
    # <-- Add ignore_https_errors=True here to bypass SSL errors
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True,    # <--- Important fix here!
    )
    yield context
    context.close()

# ✅ Shared page instance (session-wide)
@pytest.fixture(scope="session")
def page(context) -> Page:
    page = context.new_page()
    yield page
    page.close()

# ✅ Login Page Object fixture
@pytest.fixture
def login_page(page: Page):
    from pages.login_page import Loginpage  # Adjust import if needed
    login = Loginpage(page)
    login.navigate("https://demowebshop.tricentis.com/login")
    yield login

# ✅ Hook: Capture and attach screenshot to Allure on test failure
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
            
            # Save screenshot to file
            page.screenshot(path=str(screenshot_path))
            print(f"\n📸 Screenshot captured on failure: {screenshot_path}")
            
            # Attach screenshot to Allure report
            with open(screenshot_path, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
