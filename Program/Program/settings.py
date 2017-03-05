# -*- coding: utf-8 -*-

# Scrapy settings for Program project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Program'

SPIDER_MODULES = ['Program.spiders']
NEWSPIDER_MODULE = 'Program.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1 #每次请求间隔1秒

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Program.pipelines.ProgramPipeline': 300,
}

# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'douban'
MONGODB_DOCNAME = 'doubanbook'

