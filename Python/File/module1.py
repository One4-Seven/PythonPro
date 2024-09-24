import json


def user_info(path):  # 以路径作为形参 #
    if path.exists():  # 调用 exists 判断路径是否存在 返回值为 True False #
        while True:  # 路径存在 #
            show_info(path)
            choice = input("Do you want to change them? Yes or No: ")
            if choice.lower() == 'yes':
                change_info(path)
            else:
                break
    else:  # 路径不存在  #
        print("Your are the first user in this program")
        build_info(path)
        show_info(path)


def show_info(path):  # 定义打印信息函数 #
    print("These your information: ")
    json_info = path.read_text()
    user_info = json.loads(json_info)
    for key, value in user_info.items():
        print(f"{key.title()} : {value.title()}")


def build_info(path):  # 定义创建信息函数 #
    name = input("Please give me your name: ")
    location = input("Please give me your location: ")
    lover = input("Please give me your lover: ")

    user_info = {'name': name, 'location': location, 'lover': lover}
    json_info = json.dumps(user_info)  # 将要保存的数据转化为 json 格式的字符串输出 #
    path.write_text(json_info)  # 调用 write_text 函数将转换好的数据写入指定文件中 如果文件不存在则会自动创建文件  #


def change_info(path):  # 定义修改信息函数 #
    name = input("Please give me your new name: ")
    location = input("Please give me your new location: ")
    lover = input("Please give me your new lover: ")

    user_info = {'name': name, 'location': location, 'lover': lover}
    json_info = json.dumps(user_info)  # 将 json 格式的字符串转换为所需数据输出 #

    path.write_text(json_info)  # 调用 write_text 函数将转换好的数据写入指定文件中 如果文件存在则会自动清空原文件内容 #
