import scrapy


# 通过回调函数发送POST请求 解决cookie携带问题 #
class UserInfoSpider(scrapy.Spider):
    name = "User_info"
    allowed_domains = ["www.openedv.com"]
    start_urls = [
        "http://www.openedv.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"]

    def start_requests(self):
        data = {
            'username': '3230086231@qq.com',
            'password': 'shx212090123',
            'quickforward': 'yes',
            'handlekey': 'ls'
        }
        yield scrapy.FormRequest(url=self.start_urls[0], formdata=data)  # 向登录界面发送POST请求 默认回调函数为 parse #

    def parse2(self, response):
        with open('User_info.html', 'w', encoding='gbk') as fp:
            fp.write(response.text)
            print("用户好友界面存储完成")

    def parse(self, response):  # 处理第一次爬取的结果并发送新的网络请求 #
        with open('Login.html', 'w', encoding='gbk') as fp:
            fp.write(response.text)
            print("登录界面存储完成")

        new_url = "http://www.openedv.com/home.php?mod=space&do=friend"  # 新的URL会自动携带cookie #
        yield scrapy.Request(url=new_url, callback=self.parse2)  # 调用新的回调函数处理新网页的爬取结果 #
