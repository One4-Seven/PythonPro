# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ReviewUrlPipeline:
    @staticmethod
    def open_spider(spider):
        print('爬虫开始')

    def process_item(self, item, spider):
        print(item['author'])

    @staticmethod
    def close_spider(spider):
        print("爬虫结束")
