import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

# Base directory for artifacts
ARTIFACTS_DIR = Path("test-artifacts")
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance) -> Browser:
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=100)
    yield browser
    browser.close()

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

    context.tracing.stop(path=str(trace_path))
    context.close()

@pytest.fixture(scope="function")
def page(context, request) -> Page:
    page = context.new_page()
    yield page

    # Take screenshot if test fails
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_path = ARTIFACTS_DIR / f"{request.node.name}_failed.png"
        page.screenshot(path=str(screenshot_path))
        print(f"\n🖼️ Screenshot taken: {screenshot_path}")
    page.close()

# Hook to detect test failures and attach to request.node
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Get the report object for each phase (setup, call, teardown)
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
