from fastapi import FastAPI
from app.webscraper import WebScraper

app = FastAPI()

@app.get("/")
async def read_root(pages: int = 1):
    scraper = WebScraper(pages)
    df = scraper.scrape_content()
    return df.to_dict(orient='records')

