import functools
import module1  # 导入整个模块 #
import module3 as m3  # 导入整个模块并指定别名 #
from module1 import ride  # 导入模块中的指定函数 #
from module1 import time_transform as tt  # 导入模块中的指定函数并指定别名 #
from module2 import *  # 导入整个模块中的所有函数 如果存在all列表 只会导入其中的函数 #

my_add = lambda a, b: a + b  # lambda表达式简单应用 #
print(my_add)
print(my_add(1, 2))

print("一至十的平方: ")
print(list(map(lambda a: a ** 2, range(1, 11))))  # map(函数, 作用序列) 把函数作用于所有序列元素上 返回一个map对象 #

print("一至十相加: ")
print(functools.reduce(lambda a, b: a + b, range(1, 11)))  # reduce(函数, 作用序列) 把上一次运算的结果依次和序列元素运算#

print("一至十的单数: ")
print(list(filter(lambda a: a % 2 != 0, range(1, 11))))  # filter(函数, 作用序列) 用函数过滤所有序列元素 返回一个filter对象 #


def hello(username):  # 定义函数 #
    """你好,很高兴见到你"""  # 定义说明文档 #
    print(f"Hello {username.title()}, nice too meet you!")


hello('mike')
help(hello)  # 查看说明文档 #


def favourite_pet(pet, name):  # 定义函数 #
    """
    喜欢的宠物
    :param pet: 宠物类型
    :param name: 宠物名字
    :return: 综合信息
    """
    print(f"My favourite pet is {pet.title()}")
    print(f"It name is {name.title()}")


help(favourite_pet)
favourite_pet('cat', 'tom')  # 位置实参 #
favourite_pet(pet='mouse', name='jerry')  # 关键字实参 #


def favourite_food(name, food='milk'):  # 指定默认形参 #
    print(f"{name.title()}'s favourite food is {food}")


favourite_food('viper')  # 位置实参 #
favourite_food('jett', 'bread')  # 位置实参 #
favourite_food(name='fade', food='chocolate')  # 关键字实参 #

original_message = ['Hello', 'nice', 'to', 'meet', 'you']
last_message = []


def send_message(old, new):  # 定义发送消息函数 形参为列表 #
    while old:
        text = old.pop(0)
        print(f"The message {text} is sending!")
        new.append(text)


def copy_message(old, new):  # 定义复制消息函数 形参为列表 #
    for text in old:
        print(f"The message {text} is copy!")
        new.append(text)


def print_message(texts):  # 定义打印消息函数 形参为列表 #
    for text in texts:
        print(text)


send_message(original_message, last_message)

print("The original message:")
print(original_message)
print("The last message:")
print(last_message)

copy_message(last_message, original_message)

print("The original message:")
print(original_message)
print("The last message:")
print(last_message)

print_message(original_message)
print_message(last_message)


def pizza(size, *toppings):  # 创建名为 toppings 的元组接收任意数量的位置实参 (*args) #
    print(f"The pizza's size is {size} and ordering: ")
    for topping in toppings:
        print(topping.title())


pizza(12, 'butter', 'beef', 'cheese')
pizza(14, 'tomato')


def build_information(height, weight, **user_info):  # 创建名为 user_info 的字典接收任意数量的关键字实参(**kwargs) #
    user_info['height'] = height
    user_info['weight'] = weight
    return user_info


def print_information(user_info):  # 打印字典 #
    for key, value in user_info.items():
        print(f"{key.title()} -> {value}")


jack = build_information(170, 65, name='Jack', age=21, location='Su Zhou')  # 创建字典 #
mike = build_information(185, 80, name='Mike', age=23, favourite='Football')

print_information(jack)
print_information(mike)

print(module1.add('Hello ', 'Python!'))  # 调用模块函数 #
print(module1.count_number([1, 2, 3, 1, 2, 1, 2, 1], 1))
print(ride(2, 3))
print(ride('WARNING! ', 4))
tt(17, 45)

jett_info = make_personal_information('jett', age=21)  # 位置实参 关键字实参 #
jack_chen_info = make_personal_information('jack', 'chen')  # 位置实参 #
list_node_info = make_personal_information('lists', 'node', '21')  # 位置实参 #

Personal_information = [jett_info, jack_chen_info, list_node_info]  # 创建字典列表 #

select = input("Enter [Yes] to add personal information: ")  # 询问用户是否增加数据 #
if select.lower() == 'yes':  # 判断用户输入 #
    add_personal_information(Personal_information)  # 调用模块函数实现增加操作 #

show_personal_information(Personal_information)  # 调用模块函数实现打印操作 #

choice = input("Enter [Yes] to give me some music information: ")  # 询问用户是否增加数据 #
if choice.lower() == 'yes':  # 判断用户输入 #
    m3.show_music()  # 调用 module3 中的函数打印字典信息 #
