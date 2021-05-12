import scrapy
from ..items import CarrefourItem
import urllib.request
import re

import pandas as pd
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
urllib._urlopener = AppURLopener()

class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    p = 0
    start_urls = ['https://spinneys-egypt.com/en/categories/food-cupboard?page=0']

    def parse(self, response):
        items = CarrefourItem()
        newtitle = []
        img_link = response.css('.sp-product .imgwrap img::attr(data-srcset)').extract()
        title = response.css('.details h2::text').extract()

        for i in title:
            newtitle.append(i.lstrip())
        counter=0
        for a in newtitle:
            f = img_link[counter]
            f = f.split('//')

            a = re.sub(r'[^a-zA-Z0-9_\s]+', '', a)

            urllib._urlopener.retrieve("https://www." + f[1], str(a) + '.jpg')

            counter+=1

        items['img_link'] = img_link
        items['item_name'] = title

        print(len(img_link))
        yield items
        next_page = "https://spinneys-egypt.com/en/categories/food-cupboard?page="+str(DatasetSpider.p)
        if DatasetSpider.p <= 13:
            DatasetSpider.p += 1
            yield response.follow(next_page, callback= self.parse)
