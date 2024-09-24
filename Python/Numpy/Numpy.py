import numpy as np

print(np.eye(3))  # 创建一个3x3的单位矩阵 #

print(np.array([1, 2, 3]))  # 创建数组 #

print(np.array([1, 2, 3], dtype=float))  # 创建普通数组 并指定元素类型 #

print(np.zeros(10, dtype=int))  # 创建指定初始元素和类型的数组 默认为浮点数类型元素 #
print(np.ones(10))

print(np.full((4, 4), 4))  # 创建四行四列的二维数组 指定初始元素 #

print(np.arange(1, 11, 2))  # 创建线性序列数组 可以设置步长 #

print(np.linspace(1, 10, 4, dtype=int))  # 创建等差数列数组 指定初始元素 结束元素 数组元素个数 #
print(np.logspace(0, 2, 3, dtype=int))  # 创建等比数列数组 指定初始元素 结束元素 数组元素个数 #

print(np.random.random((3, 3)))  # 随机生成一个(3, 3)的数组 元素为[0, 1)间的随机数 #
print(np.random.randint(0, 10, (3, 3)))  # 随机生成一个(3, 3)的数组 元素为[0, 10)间的随机数 #
print(np.random.normal(0, 1, (3, 3)))  # 随机生成一个(3, 3)的数组 平均数为0 标准差为1 的正态分布随机数 #

array_text = np.array([10, 20, 40, 80, 100])
print(f"原数组: {array_text}")
print(f"打乱后数组: {np.random.permutation(array_text)}")  # permutation 函数会返回打乱后数组的副本 不修改原数组 #

np.random.shuffle(array_text)
print(f"打乱后数组: {array_text}")  # shuffle 函数会直接打乱原数组 #

array_text2 = np.random.randint(0, 10, (6, 6))
print("原数组: (6 x 6)")
print(array_text2)

print("切片选择后的数组:")
print(array_text2[1:4:, 1:6:2])  # 数组切片和列表相同 返回的是原数组的视图 视图的修改会影响原数组 #

print("变形后的数组: (3 x 12)")
array_text3 = array_text2.reshape(3, 12)  # 改变数组的构造 但要保证元素数量不改变 返回的是原数组的视图 视图的修改会影响原数组 #
print(array_text3)

array_text3[0][0] = 10  # 修改数组元素并检查原数组是否改变 #
print("修改后的原数组视图: (3 x 12)")
print(array_text3)
print("修改视图后的原数组: (6 x 6)")
print(array_text2)

a = np.array([[1, 2, 3], [4, 5, 6]])
print("原数组: (2 x 3)")
print(a)

b = np.array([[7, 8, 9], [10, 11, 12]])
print("原数组: (2 x 3)")
print(b)

c = np.c_[a, b]  # 行合并 返回结果是副本 #
print("行合并后的数组: (2 x 6)")
print(c)

d = np.r_[a, b]  # 列合并 返回结果是副本 #
print("列合并后的数组: (4 x 3)")
print(d)

x1, x2, x3 = np.split(array_text, [1, 3])  # 在指定下标处分割数组 在其左方切开 #
print(f"原数组: {array_text}")
print(f"分割后的数组: {x1}, {x2}, {x3}")

print("原数组: (6 x 6)")
print(array_text2)

left, middle, right = np.hsplit(array_text2, [1, 3])  # 在指定下标处按列分割数组 #
print("左半部分: ")
print(left)
print("中间部分: ")
print(middle)
print("右半部分: ")
print(right)

upper, middle, lower = np.vsplit(array_text2, [2, 4])  # 在指定下标处按行分割数组 #
print("上半部分: ")
print(upper)
print("中间部分: ")
print(middle)
print("下半部分: ")
print(lower)

print("原数组: (3 x 12)")
print(array_text3)
print("向量化操作后的数组: ")
print(array_text3 + 147)

e = np.floor(10 * np.random.random((3, 3)))  # np.floor 向下取整 #
f = np.ceil(10 * np.random.random((3, 3)))  # np.floor 向上取整 #

print("原数组: (3 x 3)")
print(e)
print("原数组: (3 x 3)")
print(f)

g = np.dot(e, f)  # 矩阵相乘 #
print("矩阵相乘: (3 x 3)")
print(g)

print("向量相乘: (3 x 3)")
print(e * f)

print("向量按行拼接: (6 x 3)")
print(np.vstack((e, f)))

print("向量按列拼接: (3 x 6)")
print(np.hstack((e, f)))

g = np.arange(0.2, 10, 0.2).reshape(7, 7)
print("原数组: (7 x 7)")
print(g)

print(f"总和: {g.sum()}")
print(f"平均数: {g.mean()}")
print(f"方差: {g.var()}")
print(f"标准差: {g.std()}")
print(f"最大值: {g.max()} 对应下标: {g.argmax()}")
print(f"最小值: {g.min()} 对应下标: {g.argmin()}")
