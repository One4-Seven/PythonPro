import scrapy

from Douban.items import DoubanItem


class AuthorViewSpider(scrapy.Spider):
    name = "Author_view"
    allowed_domains = ["www.movie.douban.com"]
    start_urls = ["https://movie.douban.com/review/best/"]

    # (终端执行) scrapy crawl 爬虫文件名称 -o 磁盘文件.后缀 进行本地化存储#
    # def parse(self, response):
    #     data_list = []
    #     div_list = response.xpath('//div[@class="review-list chart "]/div')  # 获取作者和简评的父标签 #
    #     for div in div_list:  # 遍历子标签 #
    #         author_name = div.xpath('.//header/a[2]/text()').extract_first()  # 获取作者名称 #
    #         shot_content = div.xpath('.//div[@class="short-content"]/text()').extract_first()  # 获取简评内容 #
    #         if shot_content == '\n                            ':
    #             date_dict = {'Author': author_name, 'Content': '简评内容可能剧透!!!'}
    #             data_list.append(date_dict)
    #         else:
    #             date_dict = {'Author': author_name, 'Content': shot_content}
    #             data_list.append(date_dict)
    #
    #     return data_list  # 用于本地持久化存储 #

    # 通过管道文件进行本地持久化存储 #
    def parse(self, response):
        div_list = response.xpath('//div[@class="review-list chart "]/div')  # 获取作者和简评的父标签 #
        for div in div_list:  # 遍历子标签 #
            author_name = div.xpath('.//header/a[2]/text()').extract_first()  # 获取作者名称 #
            shot_content = div.xpath('.//div[@class="short-content"]/text()').extract_first()  # 获取简评内容 #
            item = DoubanItem()  # 创建存储对象 #
            if shot_content == '\n                            ':
                item['author'] = author_name
                item['content'] = '简评内容可能剧透!!!'

            else:
                item['author'] = author_name
                item['content'] = shot_content

            yield item  # 把存储对象提交到管道 #
