# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarrefourItem(scrapy.Item):
    # define the fields for your item here like:
    item_name = scrapy.Field()
    img_link = scrapy.Field()
    item_link = scrapy.Field()

