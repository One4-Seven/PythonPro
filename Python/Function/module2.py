def make_personal_information(first, last='', age=None):  # 定义函数 #
    info = {'first': first.title(), 'last': last.title()}  # 初始化字典 #
    if age:  # 判断用户是否给出年龄 #
        info['age'] = age
    else:
        info['age'] = 'Private'
    return info


def add_personal_information(list):
    while True:  # while 循环增加字典元素 #
        first = input("PLease tell me your first_name: ")
        last = input("PLease tell me your last_name: ")

        try:
            age = int(input("PLease tell me your age: "))
        except ValueError:
            print("It means you want to hide you age !")
            age = ""

        if age == "":  # 判断用户是否给出年龄 #
            list.append(make_personal_information(first, last))
        else:
            list.append(make_personal_information(first, last, age))

        choice = input("Do you want to go? Yes or No: ")  # 询问用户是否继续添加数据 #
        if choice.lower() == 'no':
            break


def show_personal_information(list):  # 定义函数来打印字典列表 #
    for people in list:  # 遍历列表元素(字典) #
        if people['last'] == '':  # 判断用户是否有第二姓氏 #
            print(f"{people['first']}'s age is {people['age']}")
        else:
            print(f"{people['first']} {people['last']}'s age is {people['age']}")
