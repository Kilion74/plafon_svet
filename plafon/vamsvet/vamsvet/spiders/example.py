import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["vamsvet.ru"]
    start_urls = ["https://vamsvet.ru/catalog/section/svetilniki_nastennye/"]

    def parse(self, response):
        heads = response.xpath('//div[@class="prod__el"]')
        for head in heads:
            yield {
                'link': head.xpath('.//a[@class="prod__name js-cd-link"]/text()').get()
            }
