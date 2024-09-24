alien = {'color': 'red', 'point': 10}  # 初始化字典 #
new_alien = {}  # 创建空字典 #

alien_color = alien['color']
alien_point = alien['point']
print(f"the alien's color is {alien_color} point is {alien_point}")

alien['x_position'] = 15  # 添加键值对 #
alien['y_position'] = 25
print(alien)

new_alien['color'] = 'green'  # 初始化字典 #
new_alien['point'] = 5
print(new_alien)

new_alien['color'] = 'yellow'  # 修改键值对的值 键是不可修改的 #
new_alien['point'] = new_alien['point'] + alien['point']
print(new_alien)

del alien['x_position']  # 删除键值对 #
del alien['y_position']
print(alien)

lover = {  # 较长字典格式 #
    'zsy': 'hhb',
    'shx': 'yst',
    'lxy': 'hmy',
}

name = ['zsy', 'shx', 'lxy', 'cry']

for i in name:  # for 循环遍历列表 if 判断列表元素是否存在于字典中 #
    if i in lover:
        print(f"{i.title()} hava girlfriend!")
    else:
        print(f"{i.title()} dont have girlfriend!")

love = lover.get('cry', 'is single, no girlfriend!')  # get 获取键值对的值 如果不存在默认返回 None 或返回值定值 #
print(f"cry {love}")

for key, value in lover.items():  # for 循环遍历字典键值对 items 将字典转换为列表返回 元素为元组 #
    print(f"{key.title()}'s lover is {value.title()}!")

for i in lover.keys():  # for 循环遍历字典所有键值 keys (返回值为列表) #
    print(i.title())

for i in lover.values():  # for 循环遍历字典所有值 vlaues (返回值为列表) #
    print(i.title())

print(sorted(lover.items()))  # 按字典序排列所有键值对 #
print(sorted(lover.keys()))  # 按字典序排列所有键值 #
print(sorted(lover.values(), reverse=True))  # 按反字典序排列所有值 #

fruits = []
fruit_0 = {'fruit': 'apple', 'color': 'red'}
fruit_1 = {'fruit': 'orange', 'color': 'orange'}
fruit_2 = {'fruit': 'banana', 'color': 'yellow'}

for i in range(30):  # range(start,stop,step) 默认从0开始到指定数值(不含)结束 步长默认为1 #
    if i % 3 == 0:
        fruits.append(fruit_0)
    elif i % 3 == 1:
        fruits.append(fruit_1)
    else:
        fruits.append(fruit_2)

for fruit in fruits[:5]:  # for 循环遍历字典列表的前五项 #
    print(f"the fruit is {fruit['fruit'].title()}, the color is {fruit['color'].title()}")

print(f"the total of fruits is {len(fruits)}")

foods = {  # 列表字典 (嵌套) #
    'mike': ['bread', 'tea'],
    'jim': ['apple', 'milk', 'bread'],
    'tom': ['banana', 'juice', 'bread'],
}

for name, likes in foods.items():  # for 循环遍历 foods 键值对 #
    print(f"{name.title()} like eat:")
    for like in likes:
        print(like.title())

users = {  # 字典中存储字典 (嵌套) #
    'listnode': {
        'first': '申',
        'last': '恒旭',
        'location': '苏州',
    },

    '杨杨杨': {
        'first': '杨',
        'last': '思婷',
        'location': '苏州',
    },
}

for username, userinfo in users.items():
    really_name = f"{userinfo['first']}{userinfo['last']}"  # ͨ组合用户真实姓名 #
    location = userinfo['location']

    print(f"用户昵称: {username.title()}")
    print(f"真实姓名: {really_name}")
    print(f"居住地: {location}")

pet_message = [{'pet': 'cat', 'master': 'jim'}, {'pet': 'dog', 'master': 'mike', }]  # 字典列表 (嵌套) #

for i in pet_message:
    print(f"The {i['pet'].title()}'s master is {i['master'].title()}")

dictionary = {i: i ** 2 for i in range(5)}  # 字典推导式 #
print(dictionary)
print({key: value for key, value in dictionary.items() if value > 8})  # 筛选字典数据 #

l1 = ['name', 'age', 'gender']
l2 = ['yst', 18, 'woman']
dictionary = {l1[i]: l2[i] for i in range(len(l1))}  # 合并列表为字典 #
print(dictionary)