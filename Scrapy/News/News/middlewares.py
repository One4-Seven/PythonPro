import random
from time import sleep

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.http import HtmlResponse


# 设置UA池 #
class UserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(agent)
        request.headers.setdefault('User-Agent', ua)


# 设置IP池 #
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        if request.url.split(':')[0] == 'http':
            ip = random.choice(http_list)
            request.meta['proxy'] = "http://" + ip
        else:
            ip = random.choice(https_list)
            request.meta['proxy'] = "https://" + ip


# 设置下载中间件 模拟浏览器对象发送请求代替原本的请求响应体 #
class NewsDownloaderMiddleware:
    def process_response(self, request, response, spider):
        if request.url in ['https://news.163.com/world/', 'https://news.163.com/domestic/']:  # 如果是特殊URl用浏览器对象访问 #
            spider.bro.get(url=request.url)
            js = 'window.scrollTo(0, document.body.scrollHeight)'  # 编写让页面滚动到底部的js代码 #
            spider.bro.execute_script(js)  # 执行js代码 #
            sleep(2)  # 等待2s 让浏览器对象加载出新的数据 #
            page_text = spider.bro.page_source  # 获取页面数据 #
            # 返回自定义的响应体对象 #
            return HtmlResponse(url=spider.bro.current_url, body=page_text, encoding='utf-8', request=request)
        else:
            return response  # 如果是起始URL则返回本来的响应体即可 #


# 用户代理池
agent = [
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 '
    'Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 '
    'Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR '
    '2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
]

# IP池 #
http_list = ['27.185.0.164:999', '114.251.193.153:3128']
https_list = ['61.129.2.212:8080', '111.177.63.86:8888']
