import scrapy


# scrapy startproject 项目名称 #
# scrapy genspider 爬虫文件名称 起始URL #
# scrapy crawl 爬虫文件名称 (--nolog) #
class FirstSpider(scrapy.Spider):
    name = "first"  # 爬虫文件名称 用于定位到此文件 #
    allowed_domains = ["www.baidu.com"]  # 允许的域名 只能够怕至指定域名下的页面数据 #
    start_urls = ["https://www.baidu.com"]  # 起始URl 当前工程需要爬取的对应URL #

    # 爬取页面数据并进行数据解析的方法 返回值必须为迭代器或者空 #
    def parse(self, response):  # response 根据起始URL列表发起请求后获得响应对象 #
        print(response.text)
        print('执行结束')
