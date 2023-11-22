import os
import pandas as pd
from playwright.sync_api import sync_playwright, Playwright


def main(p):
    app_data_path = os.getenv("LOCALAPPDATA")
    user_data_path = os.path.join(app_data_path, "Chromium\\User Data\\Default")
    browser = p.chromium.launch_persistent_context(
        user_data_path,
        channel="chrome",
        headless=False,
        args=["--start-maximized"],
        no_viewport=True,
    )
    page = browser.new_page()
    page.goto("https://pt.pons.com/tradu%C3%A7%C3%A3o")
    page.wait_for_timeout(5000)
    browser.close()
    arq = pd.read_excel("./consulta/consulta.xlsx", header=None)
    valor = arq.iloc[0, 0]
    print(valor)


with sync_playwright() as p:
    main(p)
