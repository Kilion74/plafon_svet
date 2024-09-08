import scrapy
from scrapy_splash import SplashRequest


class ExampleSpider(scrapy.Spider):
    name = "svetilniki"
    allowed_domains = ["donplafon.ru"]
    start_urls = [f"https://donplafon.ru/catalog/svetilniki/?PAGEN_2={page}" for page in range(1, 2173)]

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
            'photo': 'https://donplafon.ru' + response.xpath('.//div[@class="productImages__big"]/img/@srcset').get(),
            'params': []
        }
        rows = response.xpath('//div[@class="row"]/div[@class="col-12 col-sm-6"]/table/tbody')
        for row in rows:
            value = row.xpath('.//tr')
            for key in value:
                params = key.xpath('.//td')
                param_1 = params[0].xpath('.//text()').get().strip()
                param_2 = params[1].xpath('.//text()').get().strip()
                all_param = param_1 + ': ' + param_2
                data['params'].append(all_param)
        yield data
