import pandas as pd
import sys
import numpy as np

df = pd.read_csv('5.1.2 数据加载与储存\data\ex5.csv')
print(df)
df.to_csv('5.1.2 数据加载与储存\data\out.csv')

df.to_csv(sys.stdout,sep="|")#sys.stdout 打印不输出到文件

#null值输出为空字符串
df.to_csv(sys.stdout,na_rep='NULL')

#不输出行索引和列索引
df.to_csv(sys.stdout,index=False,header=False)

#指定列输出
df.to_csv(sys.stdout,columns=['a','b','c'])

datas = pd.date_range('1/1/2000',periods=7)#时间索引对象
print(datas)
ts = pd.Series(np.arange(7),header=7)
ts.to_csv(sys.stdout,header=False)
