# PricingMonitoramento

```bash
$ source .venv/Scripts/activate
```

para rodar o web scraping
```bash
scrapy crawl mercadolivre -o ../../data/data.jsonl
```

para rodar o pandas
```bash
python src/transformacao/main.py
```

para rodar o streamlit
```bash
$ streamlit run src/dashboard/app.py
```