import this  # python之禅 #

# 字符串时不可修改数据类型 #
MAX = 30  # 一般常量的定义为大写 #
message1 = "hello world!"
message2 = "   love you!   "
message3 = f"{message1.upper()} {message2}"  # f 格式化输出字符串 (format) #
message4 = 'i said "you are shit."'
message5 = "text.txt"
message6 = "my favourite number is"
message7 = f"{message6}: {MAX}"
message8 = """nice to 
meet you"""  # 三引号字符串 所见即所得 #
message9 = "abcdefghijklmnop"
message10 = "apple and orange and banana and pineapple"
lists = ['tom', 'joe', 'jack']

print(message3)
print(message1.upper(), message2)  # 字符串全部大写 (全部小写 lower) (首字母大写 title) 均不改变原字符串 #
print(message4)
print(message1)
print(message5.removesuffix('.txt'))  # 删除指定前缀 (删除后缀 removeprefix) 均不改变原字符串 #
print(message5)
print(message2.lstrip())  # 删除字符串左空白 (右空白 rstrip) (两端空白 strip) 均不改变原字符串 #
print(message2)
print(5 * 3)
print(message6.find('nums'))  # 寻找指定子串 存在时返回开始下标 否则返回-1 find(子串, 开始下标, 结束下标) #
print(message6.index('num'))  # 寻找指定子串 存在时返回开始下标 否则报错 index(子串, 开始下标, 结束下标) #
print(message6.count('num'))  # 寻找指定子串 返回出现的次数 count(子串, 开始下标, 结束下标) #
print(message7)
print(message8)
print(max(message9))  # 返回最大值和最小值 #
print(min(message9))
print(message9[0])  # 通过字符串下表索引来打印元素 #
print(message9[-1])
print(message9[2:7:2])  # 字符串切片 [开始位置(包含), 结束为止(不包含), 步长(默认为1)] #
print(message9[:5])  # 前五个元素 #
print(message9[-5:])  # 最后五个元素 #
print(message9[::-1])  # 倒序遍历 #
print(float(MAX))  # 类型强转 #
print(str(MAX))
print(message10.replace('and', 'or'))  # 字符串替换 replace(被替子串换, 替换子串, 替换次数) #
print(message10.replace('and', 'or', 2))
print(message10.split('and'))  # 字符串分割 返回一个列表 split(分割符, 分割次数) #
print(message10.split('and', 2))
print(' love '.join(lists))  # 合并字符串列表 返回合并后的字符串 连接符.join(字符串列表) #
print(message9.isalpha())  # 全是字母 #
print(message9.isdigit())  # 全是数字 #
print(message9.isalnum())  # 全是字母和数字 #
print(message9.isspace())  # 全是空格 #
print('我爱南京审计大学')
