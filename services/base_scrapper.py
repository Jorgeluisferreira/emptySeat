from abc import ABC, abstractmethod
from playwright.async_api import async_playwright

class BaseScraper(ABC):
    def __init__(self, url):
        self.url = url

    async def get_vagas(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto(self.url)
            data = await self._extract(page)
            await browser.close()
            return data


    @abstractmethod
    def _extract(self, soup):
        pass
