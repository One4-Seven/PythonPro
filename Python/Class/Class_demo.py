class Base:
    def sleep(self):
        print('Base sleep')


class MonkeyBase(Base):
    pass
    # def sleep(self):
    #     print('Monkey Base sleep!')


class Monkey(MonkeyBase):
    def eat(self):
        print('eat peach!')

    # def sleep(self):
    #     print('Monkey sleep!')


class GodBase(Base):
    def sleep(self):
        print('God Base sleep!')


class God(GodBase):
    def fly(self):
        print('can fly!')

    def sleep(self):
        print('God sleep!')


class SunWuKong(Monkey, God):  # Python 支持多继承 采用独有的C3算法 结合了 #
    def play(self):
        print('SunWuKong is playing Golden-hooped Rod!')


monkey_king = SunWuKong()
monkey_king.play()
monkey_king.sleep()
print(SunWuKong.mro())  # 打印继承顺序 #
print("---------------------------------------------------------------------------------------------------------")


# @classmethod 定义类方法 形参 cls #
# @staticmethod 定义静态方法 一般用于处理与类无关数据 不能有cls参数 不能有self参数 #
# @property 定义属性方法 可以把一个实例方法转变为类属性 #

class DemoText():
    number = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.class_method()

    @classmethod
    def class_method(cls):
        cls.number = cls.number + 1

    @staticmethod
    def static_method(name):
        print(f"Hello {name}!")

    @property
    def property_method(self):
        return f"My name is {self.name}!"


demo1 = DemoText("XBOX", 200)
print(demo1.name)  # 实例属性 #
print(DemoText.number)  # 类属性 #
DemoText.static_method("SWITCH")  # 静态方法 #
print(DemoText.property_method)
print(demo1.property_method)  # 属性方法 #

if hasattr(demo1, "name"):  # 反射 映射 检测是否存在特定的属性 #
    print("The class have the {name} stats")

print(getattr(demo1, "name"))  # 获取特定属性的值 #
print(getattr(demo1, "property_method"))  # 获取特定的属性方法 可以直接使用 #
func = getattr(DemoText, "static_method")  # 获取特定方法 看情况适用 #
func("PS5")
setattr(demo1, "price", 300)  # 修改特定属性的值 #
print(getattr(demo1, "price"))


def old_game(self):
    print(f"I like play game use {self.name}!")


setattr(DemoText, "new_game", old_game)  # 绑定方法到指定类中 #
demo1.new_game()

delattr(demo1, "price")  # 删除特定属性的值 #
print("---------------------------------------------------------------------------------------------------------")


class DemoText2:
    instance = None

    def __new__(cls, *args, **kwargs):  # 创建单例模型 #
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance
        else:
            return cls.instance

    def __init__(self, name):
        self.name = name
        print("__init__() over!")

    def __call__(self):  # 实例名() 调用此方法 #
        print(f"call me {self.name}")


demo2 = DemoText2("YST")  # 创建实例时优先执行 __new__() 方法然后调用__init__() 方法 #
print(demo2, demo2.name)
demo2()

demo3 = DemoText2("LJW")
print(demo3, demo3.name)
demo3()

demo4 = DemoText2("PJY")
print(demo4, demo4.name)
demo3()
print("---------------------------------------------------------------------------------------------------------")


def __init__(self, name):
    self.name = name


class_dog = type("Dog", (object,), {"type": "Dog", "__init__": __init__})  # 通过 type 动态创建一个类 #
dog1 = class_dog("Simo")
print(class_dog)  # 查看类在内存的信息 #
print(dog1.type)
print(dog1.name)
