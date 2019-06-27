# -*- coding: utf-8 -*-
import scrapy


class Spider2Spider(scrapy.Spider):
    name = 'spider2'
    allowed_domains = ['mydomain']
    start_urls = ['http://mydomain/']

    def parse(self, response):
        pass
