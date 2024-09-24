j = 1
while j < 10:  # 打印乘法表 #
    i = 1
    while i <= j:
        print(f"{j} * {i} = {i * j}", end="\t")
        i += 1
    print()
    j += 1
else:
    print('九九乘法表')  # 循环正常结束后执行 #

message = "I want to know your name"  # 字符串相加 #
message += "\nPlease tell me : "

name = input(message)  # input 获取用户输入并转化为字符串输出 #
print(f"Hello, {name.title()}!")

while True:  # 获取用户年龄 #
    try:
        age = int(input("How old are you? "))  # int 将数据类型转换为整型 #
    except ValueError:
        print("Please give me a number, Thank you !")
    else:
        break

if age >= 18:
    print("You are Adult")
else:
    print("You are Teenage")

information = ""
active = True
print("Please give me your information")
print("Enter [Quit] to end the program")

while information.lower() != 'quit':  # 通过用户输入控制 while 循环 #
    information = input("Information: ")
    if information.lower() != 'quit':
        print(information + '\n')

while active:  # 通过标志变量控制 while 循环 #
    information = input("Information: ")
    if information.lower() != 'quit':
        print(information + '\n')
    else:
        active = False

while True:  # 通过 break 控制 while 循环 #
    information = input("Information: ")
    if information.lower() != 'quit':
        print(information + '\n')
    else:
        break

number = 1

while number <= 10:  # 通过 continue 控制 while 循环 #
    if number % 2 == 0:
        number += 1
        continue  # 程序执行 continue 会直接结束本次循环 进入下一次循环 #
    print(number)
    number += 1

items = ['mike', 'tom', 'jim']
cheak_items = []

while items:  # 调用 while 循环对列表进行操作 #
    user = items.pop()
    print(f"{user.title()} is cheaked!")
    cheak_items.append(user)

print("These users have cheaked: ")
for item in cheak_items:
    print(item.title())

books = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'a']
print(books)

books.remove('a')  # 删除列表中第一次出现的指定元素 #
print(books)

while 'a' in books:  # 通过 while 循环删除所有指定元素 #
    books.remove('a')

print(books)  # 打印列表 #

responses = {}  # 创建空字典 #
active = True

while active:
    name = input("Please tell me your name: ")
    try:
        age = input("Please tell me your age: ")
    except ValueError:
        print("Please give me a number, Thank you !")
    else:
        responses[name] = age  # 添加字典元素 #

    choice = input("Do you want to add message, Yes or No ? ")  # 获取用户输入 #

    if choice.lower() == 'no':
        active = False

for name, age in responses.items():  # 打印字典 #
    print(f"{name.title()}'s age is {age}")
