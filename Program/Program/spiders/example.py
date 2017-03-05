# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com',
       )

    def parse(self, response):
        title = response.xpath('//title/text()').extract()
        baidu = response.xpath('//input[@class="bg s_btn"]/@value').extract()
        print(title[0])
        print(baidu[0])

