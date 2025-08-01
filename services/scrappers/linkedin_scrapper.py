from base_scrapper import BaseScraper
import time

class linkedin_scrapper(BaseScraper):
    def __init__(self):
        super().__init__("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")

    async def _extract(self, page):


        await page.wait_for_selector(".modal__dismiss")
        close_modal = await page.query_selector(".modal__dismiss")
        if close_modal:
            await close_modal.click()

        vacancy = await page.query_selector('[aria-controls="job-search-bar-keywords-typeahead-list"]')
        location = await page.query_selector('[aria-controls="job-search-bar-location-typeahead-list"]')
        await vacancy.fill("Desenvolvedor Python")
        await location.fill("Rio de Janeiro")
        await page.keyboard.press("Enter")
        await page.wait_for_load_state("networkidle") # para deixar a página carregar completamente

        cards = []
        job_elements = await page.query_selector_all('[data-tracking-control-name="public_jobs_jserp-result_search-card"]')
        index = 0
        for job in job_elements:
            if index < 5:
                await job.click()
                try:
                    await page.wait_for_selector(".topcard__title") 
                    h2 = await page.query_selector(".topcard__title")
                    emp = await page.query_selector(".topcard__org-name-link")

                    cards.append({
                        "titulo": await h2.inner_text(),
                        "empresa": await emp.inner_text(),
                        "fonte": "LinkedIn",
                        "Link": page.url
                    })
                    time.sleep(1)
                    index += 1
                except Exception as e:
                    print(f"Erro ao extrair dados da vaga: {e}")
                    continue

        print(f"LinkedIn: {len(cards)} vagas encontradas")
        print(cards)

        return cards
