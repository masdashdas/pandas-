import pandas as pd
import numpy as np

# 读取ex1.csv文件
df = pd.read_csv('5.1.2 数据加载与储存\data\ex1.csv')
print(df)

df1 = pd.read_table('5.1.2 数据加载与储存\data\ex1.csv',sep=',')
print(df1)

#不指定列名
df = pd.read_csv('5.1.2 数据加载与储存\data\ex2.csv',header=None)
print(df)

#指定列名
df = pd.read_csv('5.1.2 数据加载与储存\data\ex2.csv',names=['a','b','c','d','message'])
print(df)

#指定行索引
names=['a','b','c','d','message']
df = pd.read_csv('5.1.2 数据加载与储存\data\ex2.csv',names=names,index_col='message')#index_col指定message列为行索引
print(df)

#指定多层索引
parsed = pd.read_csv('5.1.2 数据加载与储存\data\csv_mindex.csv',index_col=['key1','key2'])
print(parsed)

print(list(open('5.1.2 数据加载与储存\data\ex3.txt')))

#指定分隔符
result = pd.read_table('5.1.2 数据加载与储存\data\ex3.txt',sep='\s+')
print(result)

#跳过指定行
df = pd.read_csv('5.1.2 数据加载与储存\data\ex4.csv',skiprows=[0,2,3])
print(df)

#缺失值处理
df = pd.read_csv('5.1.2 数据加载与储存\data\ex5.csv')
print(df)
print(pd.isnull(df))

#指定缺失值
df = pd.read_csv('5.1.2 数据加载与储存\data\ex6.csv',na_values=['N','NA'])
print(df)
sentinels = {'message':['foo','NA'],'somethoing':['tow']}#自定义每行的缺失值
df = pd.read_csv('5.1.2 数据加载与储存\data\ex6.csv',na_values=sentinels)
print(df)
