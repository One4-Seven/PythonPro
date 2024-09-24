t1 = (1,)  # 创建元组即使有一个元素也需要添加逗号 #
t2 = (1, 2, 3, 4, 5)  # 初始化元组(不可变列表) #
t3 = ('a', 'b', 'c')
t4 = (1, 2, 4, [3, 5, 6], 7, 8, 9, 0)
print(t4)

t4[3][2] = 2  # 元组内部的列表数据是可以修改的 #
print(t4)

print(t3.index('a'))
print(t3.count('a'))
print(len(t3))

for value in t3:  # for 循环遍历元组 #
    print(value.upper())


def name(*args):  # *args 会创建一个元组(args)来接受任意数量的实参 #
    print(args)
    for name in args:
        print(f"Hello {name.title()}!")


name('f u c k', 'zhang san', 'li si', 'mike', 'jett')
