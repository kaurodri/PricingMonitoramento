import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.ui-search-result__content')
        
        for product in products:

            prices = product.css('span.andes-money-amount__fraction::text').get()
            cents = product.css('span.andes-money-amount__cents::text').get()

            yield {
                'brand': product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get(),
                'name' : product.css('h2.ui-search-item__title::text').get(),
                'old_prince_reais': prices[0] if len(prices) > 0 else None,
                'old_prince_centavos': cents[0] if len(prices) > 0 else None,
                'new_prince_reais': prices[1] if len(prices) > 0 else None,
                'new_prince_centavos': cents[1] if len(prices) > 0 else None
            }