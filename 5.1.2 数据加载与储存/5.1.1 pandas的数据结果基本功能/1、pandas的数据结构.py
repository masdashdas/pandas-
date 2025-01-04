import pandas as pd
import numpy as np
#Series创建及其基本属性

obj = pd.Series([4,5,6,4,1,4])
print(obj)

#获取值（没有索引）
print(obj.values)

#获取索引（没有值）RangeIndex 有序索引
print(obj.index)


obj2 = pd.Series([4,5,-7,3],index = ['d','b','a','c'])
print(obj2)

#index对象（无序索引）
print(obj2.index)

#通过索引获取值
print(obj2['a'])

#单个值返回值
obj2['d'] = 6
print(obj2[['c','a','d']])#列表返回series

#通过索引修改值筛选
obj2[obj2>0] = 0
print(obj2)

#numpy函数，exp指数函数
print(np.exp(obj2))

print(obj2*2)

#判断索引是否存在值
print('b' in obj2)

print('e' in obj2)

#字典创建series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

#指定索引
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)

#利用pandas的isnull和notnull函数判断空值
print(pd.isnull(obj4))#true表示空值

print(pd.notnull(obj4))#false表示空值

print(obj4.isnull())

#series相加，取并集，没有的为空值
print(obj3+obj4)

#series本身的属性及其索引的属性
obj4.name = 'population'
obj4.index.name ='state'
print(obj4)

#通过赋值的方式修改索引
print(obj)
obj.index=['a','b','c','d','e','f']
print(obj)

#dataFrame创建及其基本属性

data={'state':['Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002],
      'pop':[1.5,2.4,2.9]}
frame = pd.DataFrame(data)
print(frame)
#预览的ataframe的前5行数据
print(frame.head())

#更改行索引（如果多或少入值会报错）
print(pd.DataFrame(data,columns=['year','state','pop']))

#更改列索引（多传入为nan）
frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three'])
print(frame2)

print(frame2.columns)

#通过类似字典标记的方式将dataframe的列获取成为series
print(frame2['state'])

print(frame2.year)

#通过位置获取行，用loc（）行位置
frame2.loc['one']

#通过位置获取列，用iloc（）列位置
frame2.iloc[1]

#列可以通过赋值的方式修改
frame2['debt'] = 16.5#列表和数组都可以赋值
print(frame2)

print(np.arange(3.))

frame2['debt'] = np.arange(3.)
print(frame2)

#将列表或数组赋值给某个列时，长度必须一致，如果赋值的是一个series，就会精准匹配索引，所有空位会填充NaN
val=pd.Series([-1.2,-1.5,-1.7],index=['two','three','four'])
frame2['debt'] = val
print(frame2)     

#为不存在的赋值会创建新列
frame2['eastern'] = frame2.state == 'Ohio'#布尔值赋值
print(frame2)

#del方法删除列
del frame2['eastern']
print(frame2)
print(frame2.columns)
print(frame2.index)

#嵌套字典创建dataframe
pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3=pd.DataFrame(pop)
print(frame3)

print(frame3.T)#转置

s2 = pd.DataFrame(pop,index=[2001,2002,2003])
print(s2)

#series组成的字典创建dataframe
pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
frame4 = pd.DataFrame(pdata)    
print(frame4)

#如果设置了dataframe的columns的name属性，会被展示出来
frame3.index.name = 'year'
frame3.columns.name = 'state'
frame3.name = 'a'
print(frame3)

print(frame3.values)

print(frame2.values)

#索引对象
obj = pd.Series(range(3), index=['a', 'b', 'c'])
print(obj)
index = obj.index
print(index)

obj.index = ['d', 'b', 'a']
print(obj)

#index的不可变性
labels=pd.Index(np.arange(3))
print(labels)
 
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)

obj3 = pd.Series([1.5, -2.5, 1], index=labels)
print(obj2)

print(obj2.index is labels)

print(frame3)
print(frame3.columns)
print('Ohio' in frame3.columns)
print(2003 in frame3.columns)

#index可以包含重复值
dup_labels = pd.Index(['foo', 'bar', 'baz', 'foo'])
print(dup_labels)
obj3 = pd.Series(np.random.randn(4), index=dup_labels)
print(obj3)

print(obj3['foo'])