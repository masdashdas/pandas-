import pandas as pd
import numpy as np

students = pd.read_excel('5.2.1数据读取及查看\学生信息.xlsx')
print(students)

print(students.info())#返回数据信息

print(students.describe())#返回数据描述性统计信息

student_os = students['操作系统']
print(student_os)

print(pd.isnull(student_os))#判断是否有空值
print(student_os.isnull())#判断是否有空值

print(student_os.values)#返回数组

print(student_os[student_os > 82])#返回空值所在行

print(students.数据库)

print(students.columns)#返回列名

print(students.index)#返回行索引

tmp = students.reindex(columns=['姓名', '性别','年龄' ,'计算机网络','数据库', '操作系统','导论'])
print(tmp[:5])

students.loc[0, '操作系统'] = 85

students.iloc[0,'操作系统'] = 85 

students=students.dropna(3)

students = students.drop(['年龄','性别'], axis=1)
print(students.head())

students = students.sort_index(axis=0, ascending=False)
print(students.head())

students = students.sort_index(axis=1, ascending=False)
print(students.head())

students = students.sort_values(by='操作系统', ascending=False)
print(students.head())

