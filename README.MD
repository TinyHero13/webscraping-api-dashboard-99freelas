# Webcraping do 99freelas e construção de API com FastAPI

# Projeto
Este projeto realiza o web scraping do site  [99freelas](https://www.99freelas.com.br/projects), transformando os dados em uma API que retorna um JSON com essas informações.

É possivel testar a API através do link: [API JSON 99Freelas](https://freelasapi-kjytds4tca-rj.a.run.app/). Obs.: Como estou usando um tier baixo no Google Cloud, a API pode demorar para carregar ou apresentar algum erro. Se isso ocorrer, basta atualizar a página ou aguardar um pouco.

Também foi criado um dashboard no Looker Studio: [99freelas dashboard](https://lookerstudio.google.com/s/mMHuARjGlTg)

### Tecnologias e bibliotecas usadas
* Python
* FastAPI
* BeautifulSoup
* Selenium
* Pandas
* Docker
* Google Cloud

## Instalação

Para instalar as dependências, é necessário possuir docker e inserir os seguintes comandos:
```bash
docker build -t nome-da-imagem .
docker run -p 80:80 nome-da-imagem
```

Também é possível utilizar sem o Docker, mas no `main.py` será necessário retirar a palavra `app` do código:
```bash
from app.webscraper import WebScraper
```
para:
```bash
from webscraper import WebScraper
```

Após isso, baixe as dependências:
```bash
pip install -r requirements.txt
```

E rode a biblioteca FastAPI:
```bash
uvicorn main:app --reload
```

## Conecte-se comigo:

- [Portfólio](https://yasmim-portifolio.vercel.app)
- [Linkedin](https://www.linkedin.com/in/yasmim-abrahao-311491227/)