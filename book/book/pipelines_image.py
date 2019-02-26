# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/10/23 上午10:47' 

import scrapy
#from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.pipelines.images import ImagesPipeline

from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
       if item.get_name()=='BookItem':
            yield scrapy.Request(url=item.get("image_url"))
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item


