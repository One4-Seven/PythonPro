import scrapy
import scrapy_redis.pipelines
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

from Scrapy_redis.items import ScrapyRedisItem


# 分布式爬取的流程:
# 1.redis 配置文件的配置：
# bind 127.0.0.1 进行注释
# protected-mode no 关闭保护模式
# 2.redis 服务器的开启:基于配置配置文件
# 3.创建 scrapy 工程后,创建基于 crawlSpider 的爬虫文件
# 4.导入 RedisCrawlSpider 类，然后将爬虫文件修改成基于该类的源文件
# 5.将 start_urls 修改成 redis_key='XXX'
# 6.将项目的管道和调度器配置成基于 scrapy-redis 组件的对象
# ITEM_PIPELINES = {  设置管道
#     "scrapy_redis.pipelines.RedisPipeline": 400,
# }
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  设置调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_PERSIST = True
# REDIS_HOST = 'localhost'  设置远程ip地址
# REDIS_PORT = 6379  设置端口号
# 7.执行爬虫文件 控制台执行 scrapy run spider XXX.py
# 8.将起始URL放置到调度器的队列中：redis-cli 中执行 lpush 队列的名称（redis_key）起始URL
# 9.设置User-Agent 设置ROBOTSTXT_OBEY = False

class DemoSpider(RedisCrawlSpider):
    name = "Demo"
    # allowed_domains = ["www.baidu.com"]
    # start_urls = ["https://www.baidu.com"]
    # https://movie.douban.com/review/best/
    redis_key = 'names'
    link = LinkExtractor(allow=r"start?=\d+")
    rules = (Rule(link, callback="parse_item", follow=True),)

    def parse_item(self, response):
        div_list = response.xpath('//div[@class="review-list chart "]/div')  # 获取作者和简评的父标签 #
        for div in div_list:  # 遍历子标签 #
            author_name = div.xpath('.//header/a[2]/text()').extract_first()  # 获取作者名称 #
            print(author_name)
            item = ScrapyRedisItem()
            item['name'] = author_name
            yield item
