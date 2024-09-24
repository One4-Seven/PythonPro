import scrapy


class ProxySpider(scrapy.Spider):
    name = "Proxy"
    allowed_domains = ["benjiip.com"]
    start_urls = ["https://benjiip.com/"]

    def parse(self, response):
        fp = open('proxy.html', 'w', encoding='utf-8')
        fp.write(response.text)
        print('IP地址查询下载完成')