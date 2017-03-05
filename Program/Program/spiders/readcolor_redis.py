# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from Program.items import ProgramItem


class ReadcolorRedisSpider(RedisSpider):
    name = "readcolor"
    allowed_domains = ["readcolor.com"]
    start_urls = (
        'http://readcolor.com/lists',
    )
    url = 'http://readcolor.com'

    def parse(self, response):
        book_list_group = response.xpath('//article[@style="margin:10px 0 20px;"]')
        for book_list in book_list_group:
            item = ProgramItem()
            item['book_list_title'] = book_list.xpath('header/h3/a/text()').extract()[0]
            item['book_number'] = book_list.xpath('p/a/text()').extract()[0]
            book_list_url = book_list.xpath('header/h3/a/@href').extract()[0]
            yield scrapy.Request(self.url + book_list_url, callback=self.parse_book_list_detail, meta={'item': item})

    def parse_book_list_detail(self, response):
        item = response.meta['item']
        summary = response.xpath('//div[@id="list-description"]/p/text()').extract()
        item['book_list_summary'] = '\n'.join(summary)
        yield item #将item提交给pipelines处理
