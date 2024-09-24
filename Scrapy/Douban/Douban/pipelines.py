import pickle
import redis
import pymysql


# 存储到本地文件中 #
class DoubanPipeline:
    fp = None

    # 爬虫文件开始时运行一次 #
    def open_spider(self, spider):
        print("爬虫开始")
        self.fp = open('./Douban_files.txt', 'w', encoding='UTF-8')

    # 每次有新的item对象提交都会运行一次 #
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ":" + content + "\n")
        print("写入磁盘成功")

    # 爬虫文件结束时运行一次 #
    def close_spider(self, spider):
        print("爬虫结束")
        self.fp.close()


# 存储到本地数据库(MySql) #
class DoubanPipelineMySql:
    conn = None
    cursor = None

    # 爬虫文件开始时运行一次 #
    def open_spider(self, spider):
        print("爬虫开始")
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='12345', db='douban')  # 连接数据库 #

    # 每次有新的item对象提交都会运行一次 #
    def process_item(self, item, spider):
        sql = 'insert into shot_content values("%s", "%s")' % (item['author'], item['content'])  # 编写SQL语句 #
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()  # 提交事务 #
            print("写入MySql成功")
        except Exception as e:
            print(e, "写入MySql失败")
            self.conn.rollback()  # 回滚事务 #

    # 爬虫文件结束时运行一次 #
    def close_spider(self, spider):
        print("爬虫结束")
        self.cursor.close()
        self.conn.close()  # 关闭数据库连接 #


# 存储到本地数据库(Redis) #
class DoubanPipelineRedis:
    conn = None

    # 爬虫文件开始时运行一次 #
    def open_spider(self, spider):
        print("爬虫开始")
        self.conn = redis.Redis(host='127.0.0.1', port=6379)  # 连接数据库 #

    # 每次有新的item对象提交都会运行一次 #
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        data_dict = {'author': author, 'content': content}
        self.conn.lpush('data', pickle.dumps(data_dict))
        print("写入Redis完成")

    @staticmethod
    def close_spider(spider):
        print("爬虫结束")
