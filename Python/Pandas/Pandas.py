import pandas as pd
import matplotlib.pyplot as plt

# 第一种基础存储对象 Series #
a = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])  # 基于的数组来创建一个带标签的数组 #
b = pd.Series({'a': 6, 'b': 7, 'c': 8, 'd': 9, 'e': 10})  # 基于字典来创建一个序列 #
c = pd.Series({'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5})
print(a)
print('--------------------')
print(b)
print('--------------------')
print(c)
print('--------------------')
print(a + b)
print('--------------------')
print(b + c)
print('--------------------')
print(pd.isnull(b + c))  # 判断NaN #
print('--------------------')
print((b + c).notnull())
print('--------------------')
print((b + c).dropna())  # 删除NaN #
print('--------------------')
print((b + c).fillna(0))  # 填充NaN #
print('--------------------')
print(a.add(c, fill_value=0))  # 序列相加 空值用指定值代替 不会产生NaN #
print('--------------------')
print(a ** 2)
print('--------------------')
print(a[0:4:2])
print('--------------------')
print(a > 2)  # 等同于 Numpy 产生 bool 类型数组 #
print('--------------------')
print(a[a > 2])
print('--------------------')
print(f"标签切片索引: \n{a['a':'d']}")  # 通过标签切片时前后都包括 ['a', 'b'] #
print('--------------------')
print(f"下标列表索引: \n{a[[0, 3, 4]]}")
print('--------------------')
print('r' in a)
print('--------------------')
for i in a:  # 遍历序列时 value 优先 #
    print(i)
print('--------------------')
print(a.index)
print('--------------------')
print(a.values)
print('--------------------')
print(a.loc['a'], a.iloc[4])
print('--------------------')

# 第二种基础存储对象 Dataframe #
d = pd.DataFrame(
    {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([4, 5, 6, 7], index=['a', 'b', 'c', 'd'])})
e = pd.DataFrame({'one': [1, 2, 3], 'two': [4, 5, 6]}, index=['a', 'b', 'c'])
print(d)
print('--------------------')
print(e)
print('--------------------')
print(e.T)  # 转置对象 #
print('--------------------')
print(d.index)
print('---------------------')
print(d.columns)  # 获取列名称 #
print('---------------------')
print(d.describe())  # 统计列数据 #
print('--------------------')
print(d.values)
print('--------------------')
print(e['one']['c'])
print('---------------------')
print(e.loc['a', 'two'])
print('---------------------')
print(e.loc[['a', 'c'], :])
print('--------------------')
print(e.iloc[2, 1])
print('--------------------')
print(d.dropna())  # 删除NaN 会删除整行数据且存在一个即可 #
print('---------------------')
print(d.dropna(how='all'))  # 删除NaN 会删除整行数据但是要全为 NaN #
print('--------------------')
print(d.dropna(axis=1, how='any'))  # 删除NaN 会改为删除所在列所有数据 #
print('--------------------')
print(d.fillna(0))
print('---------------------')
print(d.sum())  # 对值求和 默认为列 NaN不参与计算 #
print('--------------------')
print(d.sum(axis=1))
print('--------------------')
print(d.sort_values(by=['one'], ascending=False))  # 按列的值降序排列 默认为升序 #
print('---------------------')
print(d.sort_values(by=['c'], ascending=False, axis=1))  # 按行的值降序排列 默认为升序 #
print('--------------------')
print(d.sort_index(ascending=False))  # 按行标签降序排列 #
print('--------------------')
print(d.sort_index(ascending=False, axis=1))  # 按列标签降序排列 #
print('--------------------')

# 基础时间存储对象 Datetime #
print(pd.date_range('1/1/2018', '12/31/2018', freq='ME'))  # 指定开始和结束时间 按指定间隔划分 默认为D 每一天为间隔 #
print('--------------------')
print(pd.date_range('2024-09-01', periods=8, freq='ME'))  # 指定开始时间 设置个数和间隔 #
print('---------------------')
print(pd.date_range('2024-09-01', periods=10, freq='1h20min'))
print('--------------------')
f = pd.Series(range(1000), pd.date_range('2024-09-01', periods=1000))
print(f)
print('--------------------')
print(f['2025'])  # 按索引返回所有2025年数据 #
print('--------------------')
print(f['2024-10-21': '2025-9-17'])  # 时间切片 #
print('--------------------')
print(f.resample('ME').sum())  # 把每一个月作为整体求和 #
print('--------------------')

# 读取CSV文件内容 #
df = pd.read_csv('score.csv', encoding='GBK', index_col=0,
                 na_values='NaN')  # sep 分隔符 header=None 无列名 name=[] 指定列名 #
print(df)
print('--------------------')
df.to_csv('new_score.csv', sep='-', encoding='GBK', na_rep='缺考', index=False, header=False)
print('数据更新完毕')
df.to_html('new_score.html')
print('HTML数据更新完毕')
df.to_json('new_score.json')
print('JSON数据更新完毕')
df.to_xml('new_score.xml')
print('XML数据更新完毕')
print('--------------------')
df.plot()
plt.show()
print('绘制完成')
