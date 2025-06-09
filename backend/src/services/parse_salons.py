import sys
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import time

URL = "https://zapis.kz/almaty/u/parikmaherskie-uslugi"
HTML_FILE = "zapis.html"

_cache = {"data": None, "ts": 0}

async def fetch_salons():
    if _cache["data"] and time.time() - _cache["ts"] < 300:  # 5 минут
        return _cache["data"]
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        page = await browser.new_page()
        await page.goto(URL, wait_until="networkidle")
        html = await page.content()
        await browser.close()

    soup = BeautifulSoup(html, "html.parser")
    salons = []
    for div in soup.select("div.firm-name"):
        name = div.get("title") or div.text.strip()
        address_div = div.find_next_sibling("div", class_="firm-address")
        address = address_div.get("title") or address_div.text.strip() if address_div else ""
        salons.append({"name": name, "address": address})
    _cache["data"] = salons
    _cache["ts"] = time.time()
    return salons

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        page = await browser.new_page()
        await page.goto(URL, wait_until="networkidle")
        html = await page.content()
        await browser.close()

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML saved to {HTML_FILE}")

    soup = BeautifulSoup(html, "html.parser")
    salons = []
    for div in soup.select("div.firm-name"):
        name = div.get("title") or div.text.strip()
        address_div = div.find_next_sibling("div", class_="firm-address")
        address = address_div.get("title") or address_div.text.strip() if address_div else ""
        salons.append({"name": name, "address": address})
    print(f"Found {len(salons)} salons")
    for salon in salons[:5]:
        print(salon)

if __name__ == "__main__":
    asyncio.run(main())