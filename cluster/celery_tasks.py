from celery import Celery
from scraper.core import ScrapeMaster

app = Celery('scraper', broker='redis://redis:6379/0')

@app.task(bind=True)
def scrape_task(self, url: str):
    scraper = ScrapeMaster()
    return asyncio.run(scraper.crawl(url))
