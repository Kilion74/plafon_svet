import scrapy
from scrapy_splash import SplashRequest
import six


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["donplafon.ru"]
    start_urls = [f"https://donplafon.ru/catalog/lyustry/podvesnye/?PAGEN_2={page}" for page in range(1, 669)]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        heads = response.xpath('//div[@class="productItem__container"]')
        for head in heads:
            link = 'https://donplafon.ru' + head.xpath('.//div[@class="madSlider__list"]/a/@href').get()
            if link:
                # Отправка запроса на карточку товара
                yield response.follow(link, self.parse_product)

    def parse_product(self, response):
        # Сбор полной информации о товаре
        data = {
            'name': response.xpath('//h1[@class="productInfo__title fn"]/text()').get(),
            'price': response.xpath('//div[@class="productInfo__cost productInfo__cost-new "]/text()').get(),
            'articul': response.xpath('.//div[@class="productInfo__article"]/text()').get().strip(),
            'nalichiye': response.css('.//img[@class="icon"]/text()').get().strip()

        }
        yield data
