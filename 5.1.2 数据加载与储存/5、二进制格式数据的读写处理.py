import pandas as pd
import xlrd
import openpyxl

xlsx = pd.ExcelFile('5.1.2 数据加载与储存\data\ex1.xlsx')
sheet_names = xlsx.sheet_names#获取所有sheet(工作表)名称
print(sheet_names)

df = xlsx.parse('Sheet1')#将第一行作为行索引，列索引重新生成
print(df)

df = pd.read_excel('5.1.2 数据加载与储存\data\ex1.xlsx', 'Sheet1')#不指定工作表默认第一个工作表
print(df)

writer = pd.ExcelWriter('5.1.2 数据加载与储存\data\ex2.xlsx')
df.to_excel(writer, sheet_name='Sheet1')#列索引和行索引都写入
writer.save()

df.to_excel('5.1.2 数据加载与储存\data\ex2.xlsx')#列索引和行索引都写入
