import os
import asyncio
from playwright.async_api import async_playwright
import pandas as pd


async def main():
    async with async_playwright() as p:
        app_data_path = os.getenv("LOCALAPPDATA")
        user_data_path = os.path.join(app_data_path, "Chromium\\User Data\\Default")
        browser = await p.chromium.launch_persistent_context(
            user_data_path, channel="msedge", headless=False, args=["--start-maximized"]
        )
        page = await browser.new_page()
        await page.goto("https://pt.pons.com/tradu%C3%A7%C3%A3o")
        await page.wait_for_timeout(5000)
        await browser.close()

        arq = pd.read_excel("./consulta/consulta.xlsx", header=None)
        valor = arq.iloc[0, 0]
        print(valor)


asyncio.run(main())
