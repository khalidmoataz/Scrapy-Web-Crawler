import scrapy

class Scraping(scrapy.Spider):
    name = 'Monkey'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext': title}
