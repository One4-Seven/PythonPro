import scrapy
from selenium import webdriver
from News.items import NewsItem
from scrapy_redis.spiders import RedisSpider


# Selenium 如何被应用到 scrapy
# 1.在爬虫文件中导入 webdriver 类
# 2.在爬虫文件的爬虫类的构造方法中进行了浏览器实例化的操作
# 3.在爬虫类的closed方法中进行浏览器关闭的操作
# 4.在下载中间件的 process_response 方法中编写执行浏览器自动化的操作


class DemoSpider(RedisSpider):
    name = "Demo"
    # allowed_domains = ["www.xxx.com"]
    # start_urls = ["https://news.163.com/"]
    redis_key = 'names'

    def __init__(self):
        self.bro = webdriver.Edge()
        print('爬虫开始 开始实例化Edge浏览器对象')

    def closed(self, spider):
        print('爬虫结束 关闭Edge浏览器对象')
        self.bro.quit()

    def parse(self, response):  # 从主页中解析出所需板块的URL #
        li_list = response.xpath('//div[@class="ns_area list"]/ul/li')
        index = [1, 2]
        for i in index:
            module_title = li_list[i].xpath('.//a/text()').extract_first()
            module_url = li_list[i].xpath('.//a/@href').extract_first()
            print(module_title, module_url)
            yield scrapy.Request(url=module_url, callback=self.parseSecond)  # 向每个板块的URL发送请求 #

    def parseSecond(self, response):
        div_list = response.xpath('.//div[@class="ndi_main"]/div')
        print(len(div_list))
        for div in div_list:
            title = div.xpath('.//div[@class="news_title"]/h3/a/text()').extract_first()
            content_url = div.xpath('.//div[@class="news_title"]/h3/a/@href').extract_first()
            item = NewsItem()
            item['title'] = title
            yield scrapy.Request(url=content_url, callback=self.parseThird, meta={'item': item})  # 去每个文章的URL爬取内容 #

    def parseThird(self, response):
        info = response.xpath('//div[@class="post_info"]/text()').extract_first()
        info = info.strip(' \n \t')
        item = response.meta['item']
        item['info'] = info
        yield item
