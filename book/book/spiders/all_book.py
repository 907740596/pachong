# -*- coding: utf-8 -*-
import scrapy
import re

from book.items import BookItem, BdItem


class AllBookSpider(scrapy.Spider):
    name = 'allbook'
    allowed_domains = ['www.quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/shuku/']

    def parse(self, response):
        list= response.xpath("//div[@class='tab-item clearfix']/div")
        for i in list:
            detil_url=i.xpath("./a/@href").extract_first()
            if detil_url!=None:
                detil=scrapy.Request(url=detil_url,callback=self.detil)
                yield detil
        next=response.xpath("//a[@class='next']/@href").extract_first()
        s=scrapy.Request(url=next,callback=self.parse)
        yield s
    def detil(self, response):
            image_url=response.xpath("//div[@class='detail']/a/img/@src").extract_first()
            book_name=response.xpath("//div[@class='detail']/div/h1/text()").extract_first()
            bool_jianjie=response.xpath("//div[@class='detail']/div/div/div/text()").extract_first()
            bool_jianjie=bool_jianjie.strip()
            read_url1=response.xpath("//a[@class='reader']/@href").extract_first()
            book_type = response.xpath("//a[@class='c009900']/text()").extract_first()
            booker = response.xpath("//dl[@class='bookso']/dd/text()").extract_first()
            try:
                str_list=read_url1.split('/')
                book_id=str_list[-1]
            except:
                book_id=403
            r = BookItem(image_url=image_url, book_name=book_name, bool_jianjie=bool_jianjie, book_id=book_id,
                            book_type=book_type,booker=booker)
            yield r
            text = scrapy.Request(url=read_url1, callback=self.read1, meta={'book_id': book_id})
            yield text

    def read1(self, response):
        list=response.xpath("//div[@class='clearfix dirconone']/li")
        book_id = response.meta['book_id']
        for i in list[0:31]:
            book_title=i.xpath("./a/text()").extract()
            text_url = i.xpath("./a/@href").extract_first()
            if text_url!=None:
                text = scrapy.Request(url=text_url, callback=self.text, meta={'book_id': book_id,'book_title':book_title})
                yield text

    def text(self, response):
        book_title=response.meta['book_title'][0]
        text_id=response.meta['book_id']
        book_text=response.url
        it=BdItem(book_title=book_title,book_text=book_text,text_id=text_id)
        yield it
