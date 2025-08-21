import pytest
import re
from pathlib import Path
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
from pages.login_page import Loginpage  # adjust path if needed

ARTIFACTS_DIR = Path("test-artifacts")
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


# Sanitize filenames (remove illegal characters for screenshot names)
def sanitize_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*@\[\]\s]', "_", name)


# ✅ Shared Playwright instance (session-scoped)
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
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
    )
    yield context
    context.close()


# ✅ Shared page object (session-wide)
@pytest.fixture(scope="session")
def page(context) -> Page:
    page = context.new_page()
    yield page
    page.close()


# ✅ Login Page Object fixture
@pytest.fixture
def login_page(page: Page):
    login = Loginpage(page)
    login.navigate("https://demowebshop.tricentis.com/login")
    yield login


# ✅ Hook: Screenshot on test failure
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if isinstance(page, Page):  # Only if `page` is available
            test_name = sanitize_filename(item.nodeid)
            screenshot_path = ARTIFACTS_DIR / f"{test_name}_failed.png"
            page.screenshot(path=str(screenshot_path))
            print(f"\n📸 Screenshot captured on failure: {screenshot_path}")
