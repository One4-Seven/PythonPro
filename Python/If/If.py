cars = ['audi', 'bmw', 'subaru', 'toyota']
my_cars = []

for car in cars:  # 特殊处理 bmw #
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

for car in cars:
    if car != 'bmw':
        print(car.title())
    else:
        print(car.upper())

if 'bmw' not in cars:  # 判断 bmw 是否在指定列表中 #
    print("我没有宝马,哈哈哈!")
else:
    print("我有宝马,哈哈哈!")

if 'bmw' in cars and 'audi' in cars:  # 关键字 and #
    print("我有宝马还有奥迪,哈哈哈!")

if 'subaru' in cars or 'toyota' in cars:  # 关键字 or #
    print("我有斯巴鲁或者丰田,哈哈哈!")

for car in cars:
    if car == 'bmw':
        print(f"my {car.upper()} is broken!")
    else:
        print(f"my {car.title()} is working!")

if my_cars:  # 列表判空 #
    print("我有属于自己的车,哈哈哈!")
else:
    print("我没有属于自己的车,呜呜呜!")

my_cars.append('toyota')
my_cars.append('bmw')

for car in my_cars:
    if car in cars and car == 'bmw':
        print(f"我有属于自己的车了,车型是: {car.upper()}")
    else:
        print(f"我有属于自己的车了,车型是: {car.title()}")

age = 68
price = 0

if age < 4:  # if-elif 语句块多次判断 #
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"你的年龄是: {age}  你的票价是: {price}")

print(cars)
for i in range(len(cars)):  # 清空列表 #
    cars.pop()
print(cars)

number = list(range(1, 10))  # 调用 range 函数初始化列表 range(开始位置(包含), 结束为止(不包含), 步长(默认为1))#
for i in number:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
