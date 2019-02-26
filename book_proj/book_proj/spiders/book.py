# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['www.quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/']

    def parse(self, response):
        pass
