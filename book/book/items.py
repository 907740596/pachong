# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_url= scrapy.Field()
    book_name= scrapy.Field()
    bool_jianjie= scrapy.Field()
    book_id= scrapy.Field()
    book_type= scrapy.Field()
    booker=scrapy.Field()



    def get_name(self):
        return BookItem.__name__
class BdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_title= scrapy.Field()
    book_text= scrapy.Field()
    text_id = scrapy.Field()




    def get_name(self):
        return BdItem.__name__
