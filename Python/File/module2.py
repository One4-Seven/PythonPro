def writing(path):
    info = ""
    print("Press [Quit] to end the program")

    while True:
        select = input("What do you want to write: ")
        if select.lower() == 'quit':
            break
        else:
            info += f"{select}\n"  # 将用户输入分行保存 #

    path.write_text(info)  # 调用 write_text 函数将转换好的数据写入指定文件中 如果文件存在则会自动清空原文件内容 #


def showing(path):
    print("The file's text is: ")
    print(path.read_text())  # 打印文件内容 #


def dividing():
    print("Press [Quit] to end the program")
    while True:
        first_number = input("Give me the first number: ")
        if first_number.lower() == 'quit':
            break
        second_number = input("Give me the second number: ")
        if second_number.lower() == 'quit':
            break
        try:  # try 语句块中存放可能报错的语句 #
            answer = float(first_number) / float(second_number)

        except ZeroDivisionError:  # try 语句块出错 执行 except(除零异常) 语句块内容 #
            print("You can't divide by zero!")

        except ValueError:  # try 语句块出错 执行 except(数据异常) 语句块内容 #
            print("Please input two number, thank you!")

        else:  # try 语句块正常执行后执行 else 语句块内容 #
            print(f"{first_number} / {second_number} = {answer}")


def count_words(path):  # 统计文件中的单词数 #
    try:
        print(f"{path} : {path.read_text()}")

    except FileNotFoundError:
        print(f"Sorry, the file is not exist!")

    else:
        number = len(path.read_text().split())  # 以空白为分隔符将字符串划分 返回值为列表 元素为分割后的字符串 #
        print(f"The text have {number} words")
