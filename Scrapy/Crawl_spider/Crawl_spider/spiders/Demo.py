import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# crawlspider 模版适用于分页查询爬取数据 #
class DemoSpider(CrawlSpider):
    name = "Demo"
    # allowed_domains = ["www.movie.douban.com"]
    start_urls = ["https://movie.douban.com/review/best/"]
    # 创建一个链接提取器对象 会在初始URL的响应对象中提取符合该正则表达式的所有URL #
    link = LinkExtractor(allow=r"start?=\d+")
    # 创建一个规则解析器对象 依次执行链接提取其中符合条件的URL并对响应对象调用回调函数 #
    # follow 属性表示是否在新的页面中继续执行链接提取器 #
    rules = (Rule(link, callback="parse_item", follow=True),)

    def parse_item(self, response):
        print(response)
