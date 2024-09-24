import datetime
import os
import pickle
import random
import string
import sys
import time
import json
import hashlib
import shutil
import re

import My_package.my_module3  # import 包名.模块名 #
from My_package import *  # 此方法导入包必须包含all列表 #

my_module1.xixi()
My_package.my_module3.jiji()
print('----------------------------------------------------------------------------------------------------')

print(os.getcwd())  # 获取当前Python脚本的工作目录 #
print(os.listdir())  # 获取当前Python脚本的工作目录下所有文件信息 #
print(os.name)  # 获取当前的操作系统 #
print(os.path.isabs('E:/Python/My_package'))  # 判断是否为绝对路径 #
print(os.path.dirname('E:/Python/File/daily.txt'))  # 获取路径 #
print(os.path.split('E:/Python/File/daily.txt'))  # 分割路径和文件名 #
os.system("python --version")  # 执行控制台窗口命令 #
print('----------------------------------------------------------------------------------------------------')

print(sys.path)  # 获取模块的搜索路径 第三方库等 #
print(sys.platform)  # 获取当前的操作系统 #
print(sys.version)  # 获取当前Python解释器的版本信息 #
print(sys.version_info)  # 获取当前Python解释器的详细版本信息 #
print(sys.getrecursionlimit())  # 获取最大递归层数 #
print(sys.getdefaultencoding())  # 获取解释器默认编码 #
print(sys.getfilesystemencoding())  # 获取内存数据存到文件里的默认编码 #
print('----------------------------------------------------------------------------------------------------')

timestamp = time.time()  # 获取 1970.01.01 00:00:00 至今经过的秒数 -> 时间戳 #
print(timestamp)
print(time.localtime(timestamp))  # 把时间戳转换为元组类型 默认以当前时间转换 #
UTC_timestamp = time.gmtime()  # 把时间戳转换为元组类型 默认将当前时间转换为UTC时区 即国际标准时间 #
print(UTC_timestamp)
print(time.mktime(UTC_timestamp))  # 元组类型 -> 时间戳 #
print(time.asctime())  # 默认传入time.localtime() 元组类型 -> 字符串类型 #
print(time.ctime())  # 默认传入time.time() 时间戳 -> 字符串类型 #
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 元组类型 -> 指定字符串类型 #
print('----------------------------------------------------------------------------------------------------')

print(datetime.date.today())  # 获取当前年月日 #
print(datetime.date(2002, 11, 28))
print(datetime.date.fromtimestamp(timestamp))
print(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(timestamp))
print('----------------------------------------------------------------------------------------------------')

number_list = []

for i in range(10):
    number_list.append(random.randrange(1, 10))  # [1, 10) #
print(number_list)

for i in range(10):
    number_list.append(random.randint(1, 10))  # [1, 10] #
print(number_list)

for i in range(10):
    number_list.append(random.random())  # [0, 1)之间的浮点数 #
print(number_list)

random.shuffle(number_list)  # 随机打乱列表 #
print("打乱后的列表: ")
print(number_list)
print(random.choice('YST'))  # 随机返回数据集中的字符 #
print(random.sample('YST', 2))  # 随机返回数据集中指定数量的字符 #
verification_codes = string.digits + string.ascii_uppercase + string.ascii_lowercase  # 获取数字和大小写字母的字符串集合 #
print(f"验证码: {''.join(random.sample(verification_codes, 6))}")  # 简单的验证码生成 #
print('----------------------------------------------------------------------------------------------------')

message = {"name": '申恒旭', "age": 12, "height": 180}
d_message = pickle.dumps(message)  # 序列化数据 #
print(d_message)
print(pickle.loads(d_message))  # 反序列化数据 #
pickle.dump(message, open('E:/Python/My_package/user_info.pkl', 'wb'))  # 把序列化的数据写入到指定文件中 #
print(pickle.load(open('E:/Python/My_package/user_info.pkl', 'rb')))  # 把数据反序列化后返回到程序中 #
print('----------------------------------------------------------------------------------------------------')

information = {"xixi": "嘻嘻", "haha": "哈哈", "lala": "拉拉"}
j_information = json.dumps(information)  # 序列化数据 #
print(j_information)
print(json.loads(j_information))
json.dump(information, open('E:/Python/My_package/user_info.json', 'w'))  # 把序列化的数据写入到指定文件中 #
print(json.load(open('E:/Python/My_package/user_info.json', 'r')))  # 把数据反序列化后返回到程序中 #
print('----------------------------------------------------------------------------------------------------')

m = hashlib.md5()  # 创建一个md5对象 #
m.update(b"sister")  # 跟新元素 #
print(m.digest())  # 打印加密后的二进制序列 #
print(m.hexdigest())  # 打印加密后的十六进制序列 #
m.update("纯情空姐".encode("utf-8"))
print(m.digest())
print(m.hexdigest())
print('----------------------------------------------------------------------------------------------------')

print("文件内容已拷贝")
shutil.copyfile("user_info.json", "user_info_copy.json")  # 拷贝文件内容 #
print("文件权限已拷贝")
shutil.copymode("user_info.json", "user_info_copy.json")  # 仅拷贝文件权限 #
print("文件修改信息已拷贝")
shutil.copystat("user_info.json", "user_info_copy.json")  # 仅拷贝文件修改保存信息 #
print("文件已压缩打包")
shutil.make_archive(base_name="my_package", format="zip", root_dir="../My_package")  # 压缩指定文件夹到指定路径下 #
print('----------------------------------------------------------------------------------------------------')


