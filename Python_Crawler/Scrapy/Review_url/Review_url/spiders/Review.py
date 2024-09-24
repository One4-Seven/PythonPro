import scrapy

from Review_url.items import ReviewUrlItem


class ReviewSpider(scrapy.Spider):
    name = "Review"
    allowed_domains = ["www.movie.douban.com"]
    start_urls = ["https://movie.douban.com/review/best/"]
    page_num = 1
    start = 0

    def parse(self, response):
        print('------------------')
        print(f'当前为第{self.page_num}页')
        print('------------------')
        div_list = response.xpath('//div[@class="review-list chart "]/div')  # 获取作者和简评的父标签 #
        for div in div_list:  # 遍历子标签 #
            author_name = div.xpath('.//header/a[2]/text()').extract_first()  # 获取作者名称 #
            shot_content = div.xpath('.//div[@class="short-content"]/text()').extract_first()  # 获取简评内容 #
            item = ReviewUrlItem()  # 创建存储对象 #
            if shot_content == '\n                            ':
                item['author'] = author_name
                item['content'] = '简评内容可能剧透!!!'

            else:
                item['author'] = author_name
                item['content'] = shot_content

            yield item  # 提交到管道 #

        if self.start < 80:
            self.page_num += 1
            self.start += 20
            new_url = f"https://movie.douban.com/review/best/?start={self.start}"
            # 当你进入 parse 函数时会默认请求一次 start_urls[0] 而当你在 parse 中又对 start_urls[0] 进行请求时
            # Scrapy 底层会默认过滤掉重复的 url，不会对该请求进行提交，这就是为什么 scrapy.Request 不被调用的原因 #
            yield scrapy.Request(url=new_url, callback=self.parse, dont_filter=True)  # dont_filter=True 关闭过滤掉重复请求 #
