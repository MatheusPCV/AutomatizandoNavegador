import os

def OpenBrowser(p):
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

def OpenPage(browser, link):
    page = browser.new_page()
    page.goto(link)
    page.wait_for_load_state()

    return page

