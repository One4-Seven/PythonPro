__all__ = ['make_music', 'show_music']  # all列表 #


def make_music(a, b, c=None):  # 定义函数 #
    music = {'name': a, 'song': b}
    if c:
        music['number'] = c
    return music  # 返回字典 #


def show_music():
    while True:
        name = input("name: ")
        song = input("song: ")

        try:
            number = int(input("number: "))
        except ValueError:
            number = ""

        if number == '':
            print(make_music(name, song))
        else:
            print(make_music(name, song, number))

        select = input("Press [Quit] to end the program: ")
        if select.lower() == 'quit':
            break


def haha():
    print('haha')
