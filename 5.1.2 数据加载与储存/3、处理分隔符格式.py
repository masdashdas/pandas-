import pandas as pd
import numpy as np
import csv

f = open('5.1.2 数据加载与储存\data\ex7.csv')
reader = csv.reader(f)
print(reader)

for line in reader:
    print(line)

with open('5.1.2 数据加载与储存\data\ex7.csv') as f:
    lines = list(csv.reader(f))
print(lines)

header,values = lines[0],lines[1:]
print(header)
print(values)

data_dict = {h:v for h,v in zip(header,zip(*values))}
print(data_dict)


#创建新格式
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ','
    quotechar = '"'
    quoting = csv.QUOTE_ALL
with open('5.1.2 数据加载与储存\data\ex7.csv') as f:
    reader = csv.reader(f,dialect=my_dialect)
    for line in reader:
        print(line)


#csv文件参数也可以用关键字
with open('5.1.2 数据加载与储存\data\ex7_out.csv','w') as f:
    reader = csv.reader(f,delimiter='|')

with open('5.1.2 数据加载与储存\data\mydata.csv','w') as f:
    writer = csv.writer(f,dialect=my_dialect)
    writer.writerow(('one','two','three'))
    writer.writerow(('1','2','3'))
    writer.writerow(('4','5','6'))
    writer.writerow(('7','8','9'))


