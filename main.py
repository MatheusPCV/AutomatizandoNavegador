import os
import pandas as pd
from lib.openComponents import OpenBrowser, OpenPage
from playwright.sync_api import sync_playwright, Playwright

def main(p):
    # Opening the browser and the page with the necessary link
    browser = OpenBrowser(p)
    page = OpenPage(browser, "https://pt.pons.com/tradu%C3%A7%C3%A3o-texto/ingl%C3%AAs-portugu%C3%AAs")

    arq = pd.read_excel("./consulta/consulta.xlsx", header=None)

    browser.close()

with sync_playwright() as p:
    main(p)
