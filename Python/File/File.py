from pathlib import Path  # 从模块中导入 Path 类 #
import os  # 导入文件操作模块 #
from module1 import *  # 导入模块中的所有函数 #
from module2 import *
from moudle3 import *

f = open('pi_digits.txt', 'r+')  # 创建并打开一个文件 默认为只读模式 文件不存在则会报错 open(文件名路径, 访问模式) #
print(f.read(4))  # 默认读取文件所有内容 返回字符串 可以指定字节数读取 #
print(list(f.readline()))  # 读取文件中一行的内容 返回字符串 #
f.seek(2, 0)  # 调整文件指针位置 seek(偏移量, 起始位置) #
print(f.readlines())  # 以换行符分割读取文件所有内容 返回列表 每一行为一个元素 #
f.close()

pi_path = Path('pi_digits.txt')  # 创建路径(相对路径) #
message1 = pi_path.read_text()  # 调用 read_text 方法会读取文件的所有内容并转换为字符串输出 #
print(message1)

pi = ""  # 创建空串 #
for line in message1.splitlines():  # 以换行符为分隔符将字符串划分 返回值为列表 元素为分割后的字符串 #
    pi += line.lstrip()
print(pi)
print(len(pi))

hello_path = Path('text_files/hello.txt')  # 创建路径(相对路径) #
message2 = hello_path.read_text()
print(message2)

nice_path = Path('E:/Python/File/text_files/nice.txt')  # 创建路径(绝对路径) #
message3 = nice_path.read_text().rstrip()
print(message3)

pet_path = Path('text_files/pets.txt')
pets = pet_path.read_text()
print(pets.splitlines())
print(f"The word 'cat' appear {pets.lower().count('cat')} times in the text")  # 调用 count 函数统计字符串中指定元素出现的次数 #

pets = pets.replace('cat', 'tom').title().splitlines()  # 调用 replace 函数对字符串中的指定元素进行替换 #
print(pets)

# os.mkdir('text_files')  # 创建文件夹 rmdir(文件夹名) 删除文件夹 #
print(os.getcwd())  # 获取当前文件夹操作路径 #
# os.chdir('text_files')  # 修改默认文件目录 #
print(os.listdir('text_files'))  # 获取指定文件夹下的所有目录 #

files_list = ['none.txt', 'tt.txt', 'text_files/hello.txt', 'pi_digits.txt']  # 初始化路径(实例)列表 #
for file in files_list:
    path = Path(file)  # 创建路径(实例) #
    count_words(path)  # 调用 module2 中的函数 #

write_path = Path('text_files/write.txt')  # 创建路径(实例) #
select = input("Do you want to writing? Yes or No: ")
if select.lower() == 'yes':
    writing(write_path)  # 调用 module2 中的函数 #
    showing(write_path)

choice = input("Do you want to calculate division between two numbers? Yes or no: ")
if choice.lower() == 'yes':
    dividing()  # 调用 module2 中的函数 #

user_path = Path('user_info.json')  # 创建路径(实例) #
user_info(user_path)  # 调用 module1 中的函数 #

signal = input("Do you want to backups some files? Yse or No: ")
if signal.lower() == 'yes':
    backups()  # 备份文件 #
else:
    print("Thanks for you choice!")
