import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # Extraer titulo (title) y nombre de paises (countries)
        title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a/text()').getall()

        # devolver la data extraida
        yield {
            'titles': title,
            'countries': countries,
        }