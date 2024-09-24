from random import randint  # 导入 Python 标准库中的函数 #
from random import choice as cc


class Six_die:
    def __init__(self):
        self.sides = 6
        print("")

    def roll_die(self):
        self.sides = randint(1, 6)  # 返回两个整数(含)之间的随机值 #

    def show_sides(self):
        print(f"The six dice's number is {self.sides}")


class Ten_die:
    def __init__(self):
        self.sides = 10
        print("")

    def roll_die(self):
        self.sides = randint(1, 10)

    def show_sides(self):
        print(f"The ten dice's number is {self.sides}")


class Ticket:
    def __init__(self):
        self.answer = [1, 4, 7, 'YST']
        self.choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'SHX', 'YST', 'PJY', 'LJW', 'FJY']
        self.my_choice = []
        self.count = 0

    def buy_ticket(self):
        self.my_choice = []
        for i in range(0, len(self.answer)):
            self.my_choice.append(cc(self.choices))  # choice 函数在指定列表或元组中随机选择一个元素返回 #
        self.count += 1

    def check_ticket(self):
        right_count = 0
        for answer in self.answer:
            if answer in self.my_choice:
                right_count += 1
        if right_count == len(self.answer):
            return True
        else:
            return False

    def show_count(self):
        print(f"The odds of winning the lottery is 1 / {self.count}")
