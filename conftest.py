import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
from pages.login_page import Loginpage  # adjust if needed

ARTIFACTS_DIR = Path("test-artifacts")
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

# Shared Playwright instance
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

# Launch browser once
@pytest.fixture(scope="session")
def browser(playwright_instance) -> Browser:
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=100)
    yield browser
    browser.close()

# Shared context across all tests
@pytest.fixture(scope="session")
def context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},  # Maximize browser window
    )
    yield context
    context.close()

# Shared page across all tests
@pytest.fixture(scope="session")
def page(context) -> Page:
    page = context.new_page()
    yield page
    page.close()

# Login page fixture
@pytest.fixture
def login_page(page):
    login = Loginpage(page)
    login.navigate("https://demowebshop.tricentis.com/login")
    yield login

# Screenshot on failure (now must handle session-scoped page)
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = ARTIFACTS_DIR / f"{item.name}_failed.png"
            page.screenshot(path=str(screenshot_path))
            print(f"\n🖼️ Screenshot taken: {screenshot_path}")
