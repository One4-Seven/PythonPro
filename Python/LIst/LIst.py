import math
import cmath

message = ['love', 'hate', 'never']
print(message)
print(message[-1])

for i, e in enumerate(message, start=1):  # 列举所有元素 默认下表为0开始 返回值为元素是元组的列表 类似于items #
    print(f'{i}: {e}')

print(message.index('hate'))  # 在列表中查找指定元素 返回下标 不存在时报错 #
print(message.count('hate'))  # 寻找指定元素 返回出现的次数 #

print('love' in message)  # 判断指定元素是否存在于列表中 #
print('love' not in message)

message.insert(2, 'always')  # 在列表中指定位置插入元素 #
print(message)

del message[2]  # 删除指定位置元素 #
print(message)

message.insert(3, 'love')  # 在列表中指定位置插入元素 #
print(message)

print(list(set(message)))  # set 将列表转换为集合来对元素进行去重 最后在转换回列表输出 #

print(message)  # 检查列表 #

message.remove('love')  # 删除列表中第一次出现的指定元素 不存在则会报错 #
print(message)

message.pop()  # 默认弹出列表末尾元素并返回它的值 #
print(message)

message.pop(0)  # 弹出指定位置元素并返回 #
print(message)

message.append('like')  # 在列表末尾添加元素 #
print(message)

message.extend('hahaha')  # 在列表末尾追加元素 并且拆分追加元素 #
message.extend(['ha', 'ha', 'ha'])
print(message)

message = ['love', 'hate', 'never', 'always', 'like']
print(message)

message.sort()  # 调用 sort 函数对列表进行升序排序 函数返回值为 None sort(排列规则(函数), 升降序) #
print(message)

message.sort(reverse=True)  # 修改 reverse 参数 进行降序排序 #
print(message)

print(sorted(message))  # 调用 sorted 函数对列表进行升序排序 函数返回值为排序后的列表 不改变原列表 #

print(sorted(message, reverse=True))  # 修改 reverse 参数 进行降序排序 #

print(message)  # 检查列表 #

message.reverse()  # 调用 reverse 函数反转列表 #
print(message)

print(len(message))  # 打印列表长度 #

goods = ['apple', 'orange', 'football', 'basketball', 'sakura']

for good in goods:  # 调用 for 循环遍历列表 #
    print(good.title())
    print(good.title() + " is my favourite!")
print("the item is over.")

number = []
square = []
square_root = []

for i in range(1, 11):  # for 循环遍历 range #
    number.append(i ** 2)
print("一至十的平方:")
print(number)

square = [value ** 2 for value in range(1, 11)]  # 列表推导式 #
print(square)

cube = [value ** 3 for value in range(1, 11)]  # 列表推导式 #
print("一至十的立方:")
print(cube)

print("number 中的最大值,最小值,总和:")
print(f"MAX:{max(number)}")
print(f"MIN:{min(number)}")
print(f"SUM:{sum(number)}")

print(number[0:9:2])  # 列表切片 起始索引为0 终止索引为9(不含) 步长为2 #
print(number[:5])  # 返回前五个元素 #
print(number[5:])  # 返回索引为5的元素至列表结尾 #
print(number[-5:])  # 返回最后五个元素 #
print(number[::-1])  # 当步长设置为负数时 默认起始索引和终止索引交换 #

for i in number[:-6:-1]:
    square_root.append(pow(i, 1 / 2))  # 调用内置函数 pow 对指定底数进行指定指数的运算 返回值类型为 float #
    square_root.append(math.sqrt(i))  # 调用 math 库中的 sqrt 函数对指定数开方 返回值类型为 float #
    square_root.append(cmath.sqrt(i))  # 调用 cmath 库中的 sqrt 函数对指定数开方 返回值类型为 complex(复数) #
print(square_root)

print("the first three numbers in the lists are:")
print(number[:3])
print("the first three numbers in the middle of the lists are:")
print(number[3:6])
print("the last three numbers in the lists are:")
print(number[-3:])

my_pizza = ['a', 'b', 'c']
friend_pizza = my_pizza[:]  # 列表复制 #
new_friend_pizza = my_pizza.copy()  # 列表复制 #

my_pizza.append('d')
friend_pizza.append('e')
new_friend_pizza.extend('def')

print(f"my favorite pizza are: {my_pizza}")
print(f"my friend's favorite pizza are: {friend_pizza}")
print(f"my new friend's favorite pizza are: {new_friend_pizza}")
