from die import *  # 导入 die 模块中的所有类 #
from gas_car import Gas_car  # 导入模块中的指定类 #
from elelctric_car import Electric_car as Ec  # 导入模块中的指定类并指定别名 #


class Restaurant:  # 创建类 #
    def __init__(self, name, type):  # 构造方法 #
        self.name = name.title()  # 初始化属性值 #
        self.type = type
        self.served = 0  # 指定默认属性值 #

    def destribe(self):  # 所有方法需要传入形参 self #
        print(f"\nThe restaurant's name is {self.name} and the type is {self.type}")

    def open(self):
        print("The restaurant is opening!")

    def close(self):
        print("The restaurant is closing!\n")

    def set_served(self, number):
        if number > self.served:
            self.served = number

    def up_served(self, number):
        if number > 0:
            self.served += number

    def increase_served(self):
        self.served += 10

    def empty_served(self):
        self.served = 0

    def show_served(self):
        print(f"The number of {self.served} people have served the restaurant")


restaurant = Restaurant('cocoon', 'chinese')  # 创建实例 #

print(restaurant.name)  # 打印实例属性 #
print(restaurant.type)
print(restaurant.served)

restaurant.destribe()  # 调用实例方法 #
restaurant.open()

restaurant.show_served()

restaurant.set_served(10)
restaurant.show_served()

restaurant.up_served(5)
restaurant.show_served()

restaurant.increase_served()
restaurant.show_served()

restaurant.empty_served()
restaurant.show_served()

restaurant.close()


class Tastes:  # 创建类 #
    def __init__(self, number=10):
        self.taste = number

    def show_custom(self):
        print(f"Today can get {self.taste * 5} customs")

    def cheak_taste(self):
        if self.taste <= 10:
            self.taste = 20

    def up_taste(self, number):
        if number > 0:
            self.taste += number

    def cempty_taste(self):
        self.taste = 0


class IceCreamstand(Restaurant):  # 创建子类继承父类 #
    def __init__(self, name, type):  # 重写构造方法 #
        super().__init__(name, type)  # 调用父类中的构造方法 #
        self.tastes = Tastes()  # 指定默认属性值 #

    def destribe(self):  # 重写父类方法 #
        print(f"\nThe icecreamstand's name is {self.name} and the type is {self.type}")

    def open(self):
        print("The icecreamstand is opening!")

    def close(self):
        print("The icecreamstand is closing!\n")


ice_creamstand = IceCreamstand('honey snow ice city', 'iceceam')  # 创建实例 #

print(ice_creamstand.name)  # 打印实例属性 #
print(ice_creamstand.type)
print(ice_creamstand.served)  # 继承的属性值 #
print(ice_creamstand.tastes)

ice_creamstand.destribe()  # 调用实例方法 #
ice_creamstand.open()

ice_creamstand.tastes.show_custom()

ice_creamstand.tastes.cheak_taste()
ice_creamstand.tastes.show_custom()

ice_creamstand.tastes.up_taste(10)
ice_creamstand.tastes.show_custom()

ice_creamstand.tastes.cempty_taste()
ice_creamstand.tastes.show_custom()

ice_creamstand.close()

my_car = Gas_car('faw', 'toyota', 2024)  # 创建实例 #
your_car = Ec('gac', 'bmw', 2024)

my_car.describe()  # 调用实例方法 #

my_car.gas.set_gas(120)
my_car.gas.show_range()

my_car.gas.up_gas(30)
my_car.gas.show_range()

my_car.gas.down_gas(100)
my_car.gas.show_range()

your_car.describe()  # 调用实例方法 #

your_car.battery.show_range()

your_car.battery.update_battery()
your_car.battery.show_range()

six_die = Six_die()  # 创建实例 #

six_die.show_sides()  # 调用实例方法 #
six_die.roll_die()
six_die.show_sides()

ten_die = Ten_die()  # 创建实例 #

ten_die.show_sides()  # 调用实例方法 #
ten_die.roll_die()
ten_die.show_sides()
print("")

lottery_ticket = Ticket()  # 创建实例 #

while not lottery_ticket.check_ticket():  # while 循环计算彩票中奖概率 #
    lottery_ticket.buy_ticket()

lottery_ticket.show_count()  # 调用实例方法 #

sport_lottery = Ticket()  # 创建实例 #

while True:  # while 循环计算彩票中奖概率 #
    sport_lottery.buy_ticket()
    if sport_lottery.check_ticket():
        break

sport_lottery.show_count()  # 调用实例方法 #
