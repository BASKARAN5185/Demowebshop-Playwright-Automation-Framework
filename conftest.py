import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
from pages.login_page import Loginpage  # adjust if needed

ARTIFACTS_DIR = Path("test-artifacts")
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

# Playwright instance shared for the session
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

# Launch a single browser for the whole test session
@pytest.fixture(scope="session")
def browser(playwright_instance) -> Browser:
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=100)
    yield browser
    browser.close()

# Create a new browser context for each test for isolation
@pytest.fixture(scope="function")
def context(browser, request) -> BrowserContext:
    test_name = request.node.name.replace("/", "_")
    trace_path = ARTIFACTS_DIR / f"{test_name}_trace.zip"

    context = browser.new_context(
        record_video_dir=str(ARTIFACTS_DIR),
        record_har_path=str(ARTIFACTS_DIR / f"{test_name}.har"),
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    # Stop tracing and save artifacts
    context.tracing.stop(path=str(trace_path))
    context.close()

# Page fixture: tied to the test's context
@pytest.fixture(scope="function")
def page(context, request) -> Page:
    page = context.new_page()
    yield page

    # Take screenshot only on test failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_path = ARTIFACTS_DIR / f"{request.node.name}_failed.png"
        page.screenshot(path=str(screenshot_path))
        print(f"\n🖼️ Screenshot taken: {screenshot_path}")

    page.close()

# Login page object fixture
@pytest.fixture
def login_page(page):
    login = Loginpage(page)
    login.navigate("https://demowebshop.tricentis.com/login")
    yield login

# Hook to track test results (used to detect failures)
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
