import asyncio
from scrappers.linkedin_scrapper import linkedin_scrapper

async def main():
    scraper = linkedin_scrapper()
    vagas = await scraper.get_vagas()
    for v in vagas:
        print(v)

asyncio.run(main())
