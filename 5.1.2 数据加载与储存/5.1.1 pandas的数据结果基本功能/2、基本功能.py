import pandas as pd
import numpy as np

#重新索引
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

obj3=pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
obj4=obj3.reindex(range(6), method='ffill')#ffill向前填充 bfill向后填充
print(obj4)

#对dataframe进行重新索引
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'e'], columns=['Ohio', 'Texas', 'California'])
print(frame)

frame2 = frame.reindex(['a', 'b', 'c', 'd'])#对行重新索引
print(frame2)#有nan值数据类型会变为float

frame3 = frame.reindex(columns=['Texas', 'California', 'Florida', 'New York'])#对列重新索引
print(frame3)

#丢弃series中指定轴上的项
obj = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(obj)

obj2 = obj.drop('c') #返回一个新的Series对象，原始对象不变
print(obj2)

print(obj.drop(['d', 'c']))

#对dataframe进行丢弃指定轴上的项
frame = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
print(frame)

#axis=0表示对行进行丢弃
print(frame.drop(['Colorado', 'Ohio'],axis=0))
print(frame.drop(['Colorado', 'Ohio']))#不传入axis参数，默认对行进行丢弃

#axis=1表示对列进行丢弃
print(frame.drop('two',axis=1))
print(frame.drop(['two', 'four'],axis=1))

#直接修改不返回新的对象
obj.drop('c', inplace=True)
print(obj)

#索引、选取和过滤
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)

print(obj['b'])
print(obj.iloc[1])

print(obj[['b','a','d']])
print(obj.iloc[[1,3]])

print(obj.iloc[0:2])#不包含末端索引
print(obj['a':'c'])#包含末端索引

#布尔索引
print(obj<2)
print(obj[obj<2])#选择值小于2的项

#dataframes的索引和选取
frame = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
print(frame)

print(frame['two'])
print(frame[['one','three']])
print(frame[:2])

print(frame[frame['three']>5])

print(frame<5)
print(frame[frame<5])
f=frame[frame<5]=0
print(f)

#loc和iloc选取
print(frame.loc['Colorado', ['two', 'three']])#索引
print(frame.iloc[2, [3,0,1]])#索引位置
print(frame.iloc[[1,2],[3,0,2]])

print(frame.loc[:'Utah', 'two'])#切片
print(frame.iloc[:,:3])#切片

print(frame.iloc[:,:3][frame.three>5])

#整数索引
ser = pd.Series(np.arange(3.))
print(ser)

print(ser[0])
# print(ser[-1])报错

ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print(ser2)

# print(ser2[-1])

print(ser[:1])
print(ser.loc[:1])
print(ser.iloc[:1])

#算术运算和数据对齐
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])  
print(s1)
print(s2)
print(s1+s2)

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'California'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2)

print(df1+df2)

df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1)
print(df2)  
print(df1+df2)

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
print(df1)  
print(df2)  
print(df1+df2)
print(df1.add(df2, fill_value=0))#fill_value为0表示对缺失值填充0后进行计算

print(df1.reindex(columns=df2.columns, fill_value=0))

arr = np.arange(12.).reshape((3, 4))
print(arr[0])
print(arr-arr[0])

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print(series)
print(frame-series)

series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(series2)
print(frame+series2)

series3 = frame['d']
print(series3)
print(frame)
print(frame-series3)#默认匹配列索引进行计算
print(frame.sub(series3, axis='index'))#匹配行索引进行计算,axis='0'和axis='index'都可以

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))#绝对值

#apply方法
f = lambda x: x.max() - x.min()
print(frame.apply(f))#默认对每一列进行计算
print(frame.apply(f, axis='columns'))#对每一行进行计算

def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
print(frame.apply(f))

#applymap方法
format = lambda x: '%.2f' % x
print(frame.applymap(format))#对每一个元素进行格式化

print(frame['e'].map(format))#对指定列的元素进行格式化

#排序与排名
#默认升序排序
obj = pd.Series(range(4), index=['d', 'b', 'a', 'c'])
print(obj)
print(obj.sort_index())#按索引排序

frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
print(frame)
print(frame.sort_index())#按索引排序
print(frame.sort_index(axis=1))#按列索引排序
print(frame)
print(frame.sort_index(axis=1, ascending=False))#按列索引降序排序

#按值排序
print(obj.sort_values())#按值排序

obj = pd.Series([4,np.nan, 7, -3,2])
print(obj.sort_values())#nan值排在最后

frame = pd.DataFrame({'b': [4, np.nan, 7, -3, 2], 'a': [0, 1, 0, 1, 0]})
print(frame)
print(frame.sort_values(by='b'))#按列b的值排序
print(frame.sort_values(by=['a', 'b']))#先按列a的值排序，再按列b的值排序

#排名
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())#默认相同数按平均值排名
print(obj.rank(method='first'))#默认method='average'
#method='min'，最小值排名
#method='max'，最大值排名
#method='first'，第一个值排名

frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
print(frame)
print(frame.rank(axis='columns'))#按列排名
print(frame.rank())

#带有重复标签的轴索引
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj)
print(obj.index)
print(obj.index.is_unique)#判断索引是否唯一
print(obj['a'])#重复标签索引，返回Series对象
print(obj['c'])#非重复标签索引，返回单个值

df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df)
print(df.loc['b'])#重复标签索引，返回DataFrame对象
