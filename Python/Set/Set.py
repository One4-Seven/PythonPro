# 集合 去重 无序 可变 #
s1 = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
print(s1)

s2 = set()  # 创建空集合 #
print(s2)
print(type(s2))

s3 = {}  # 默认是字典类型 #
print(s3)
print(type(s3))

s4 = set('dafeasadwsa')
print(s4)

s1.add(20)  # 添加单一元素 #
s1.add(20)
print(s1)

s1.update([10, 20, 30, 40, 50])  # 添加一个元素序列 #
s1.update([10, 20, 30, 40, 50])
print(s1)

print(10 in s1)
print(10 not in s1)

s1.remove(10)  # 删除指定元素 不存在则会报错 #
print(s1)

s1.discard(20)  # 删除指定元素 不存在不会报错 #
s1.discard(20)
print(s1)

print(s1.pop())  # 随机删除一个元素并返回 #
print(s1.pop())
print(s1)