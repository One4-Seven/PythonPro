try:  # 捕获指定类型的异常 #
    print(name)
except NameError:  # 捕获多个异常  元组(异常1, 异常2... ) #
    print("命名错误!")

print('------------------------------------------------------------')
try:
    file = open('test1.txt', 'r')
except FileNotFoundError as result:  # 捕获异常描述信息 #
    print(f'文件不存在: {result}')

print('------------------------------------------------------------')
try:
    num = 1 / 0
except Exception as result:  # 捕获所有异常 #
    print(result)

print('------------------------------------------------------------')
try:
    print('SecretBase~')
except Exception as result:
    print(result)
else:  # 没有发生异常时执行 #
    print("No Exception")

print('------------------------------------------------------------')
try:
    file = open('test.txt', 'r')
except FileNotFoundError as result:
    print(f'文件不存在: {result}')
    file = open('test.txt', 'w')
else:
    print('No Exception')
finally:  # 语句是否异常都会执行 #
    file.close()

print('------------------------------------------------------------')
try:  # 异常传递模型 #
    file = open('test.txt', 'r')
    try:
        while True:
            message = file.readline()
            if message == '':
                break
            # time.sleep(1)  # 程序暂停1s #
            print(message[0])
    except:
        print('程序异常终止!')
    finally:
        file.close()

except Exception as result:
    print(f'文件不存在: {result}')

print('------------------------------------------------------------')


class LengthError(Exception):  # 自定义异常 #
    error = 0  # 类属性 #

    def __init__(self, input_length):  # 魔法方法 #
        self.min_length = 3  # 对象属性 #
        self.length = input_length

    def __str__(self):  # 定义异常信息 #
        return f'你输入的密码长度为: {self.length}, 最短密码长度: {self.min_length}'

    def __del__(self):  # 对象被销毁时执行 #
        print('Bye~')

    @classmethod  # 类方法 只能调用类属性 #
    def error_count(cls):
        cls.error += 1
        print(f'错误次数: {cls.error}')

    @staticmethod  # 静态方法 不能调用类属性和对象属性 #
    def hello():
        print('Hello~')


LengthError.hello()
while True:  # 测试自定义异常 #
    try:
        password = input('Please input your password: ')
        length = len(password)
        if length < 3:
            raise LengthError(length)  # 抛出异常 #
    except LengthError as e:
        print(e)
        e.error_count()
    else:
        print('密码设置成功!')
        break
