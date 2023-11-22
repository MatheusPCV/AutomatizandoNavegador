from playwright.sync_api import sync_playwright, Playwright
import os


def openBrowser(p):
    app_data_path = os.getenv("LOCALAPPDATA")
    user_data_path = os.path.join(app_data_path, "Chromium\\User Data\\Default")
    browser = p.chromium.launch_persistent_context(
        user_data_path,
        channel="chrome",
        headless=False,
        args=["--start-maximized"],
        no_viewport=True,
    )

    return browser
