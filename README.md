# PricingMonitoramento
Este README fornece uma visão geral clara e detalhada do projeto.

<!-- incluindo a arquitetura, a estrutura de diretórios, as instruções de instalação e uso, além dos módulos específicos para extração, transformação e visualização de dados. -->

## Uma ETL em Python para Monitoramento de Preço

- Solução em Python para estratégias de pricing
- Temos uma pipeline e uma ETL em Python que coleta, consolida e gera insights
sobre determinada cadeira de produtos

## Arquitetura
Uma ETL em Python para Web Scraping

- Extração - Scrapy
- Transformação e Load - Pandas
- Dashboard - Streamlit
- Banco de dados - Postgres

## Terminal
```bash
$ source .venv/Scripts/activate
```

para rodar o web scraping
```bash
$ scrapy crawl mercadolivre -o ../../data/data.jsonl
```

para rodar o pandas
```bash
$ python src/transformacao/main.py
```

para rodar o streamlit
```bash
$ streamlit run src/dashboard/app.py
```

## Lost
```bash
$ pyenv local 3.12.1
```
```bash
$ python -m venv .venv
```
```bash
$ source .venv/Scripts/activate
```
```bash
$ pip install scrapy
```
```bash
$ scrapy startproject coleta
```
```bash
$ cd coleta/
```
```bash
$ scrapy genspider mercadolivre https://lista.mercadolivre.com.br/tenis-corrida-masculino
```
```bash 
$ scrapy shell #abrir terminal
```
```bash
$ exit() #fechar terminal
```