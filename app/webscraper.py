from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from datetime import datetime, timedelta
from selenium import webdriver


class WebScraper:
    def __init__(self, pages):
        self.url = 'https://www.99freelas.com.br/projects?page='
        self.pages = pages
        self.df = pd.DataFrame(columns=['titulo', 'categoria', 'nivel', 'data_publicado', 'propostas', 'interessados', 'descricao'])
        self.today = datetime.today()
        self.time_units = {
            'dia': 'days',
            'dias': 'days',
            'minutos': 'minutes',
            'minuto': 'minutes',
            'horas': 'hours',
            'hora': 'hours'
        }

    def parse_page(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser') 
        tables = soup.find_all('li')
        data = []
        for rows in tables:
            titulo = rows.find('h1', class_='title').get_text().strip('\n')
            infos = rows.find('p', class_='item-text information').get_text().strip().replace('\n', '').replace('\t', '').split('|')
            category = infos[0].strip()
            level = infos[1].strip()
            published = infos[2].strip().split('Publicado:')[1]
            for unit, arg in self.time_units.items():
                if unit in published:
                    amount = int(published.split(' ')[0])
                    days = self.today - timedelta(**{arg: amount})
            if 'às' in published:
                days = datetime.strptime(published, '%d/%m/%Y às %H:%M')
            if 'agora mesmo' in published:
                days = self.today

            binds = infos[4].strip().split(' ')[1]
            interested = infos[5].strip().split(' ')[1]
            description = rows.find('div', class_='item-text description formatted-text').get_text().strip()
            
            data.append({
                'titulo': titulo,
                'categoria': category,
                'nivel': level,
                'data_publicado': days,
                'propostas': binds,
                'interessados': interested,
                'descricao': description
            })
            
        return pd.DataFrame(data)
    
    def scrape_content(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        browser = webdriver.Firefox(options=options)
        all_data = pd.DataFrame(columns=['titulo', 'categoria', 'nivel', 'data_publicado', 'propostas', 'interessados', 'descricao'])
        for i in range(1, self.pages + 1):
            browser.get(f'{self.url}{i}')
            sleep(3)
            html_content = browser.page_source
            page_data = self.parse_page(html_content)
            all_data = pd.concat([all_data, page_data], ignore_index=True)
        return all_data
    
if __name__ == '__main__':
    scraper = WebScraper(200)
    df = scraper.scrape_content()
    df.to_csv('freelas.csv')