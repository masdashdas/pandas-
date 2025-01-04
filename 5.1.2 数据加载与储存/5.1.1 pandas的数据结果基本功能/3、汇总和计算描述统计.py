import pandas as pd
import numpy as np

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                    [np.nan, np.nan], [0.75, -1.3]], 
                    index=['a', 'b', 'c', 'd'], 
                    columns=['one', 'two'])

print(df)
print(df.sum())#默认按列求和
print(df.sum(axis='columns'))
#NA值会自动被排除，除非整个切片都是NA。通过skipna参数可以禁用此功能
print(df.mean(axis='columns', skipna=False))

#间接统计方法
print(df.idxmax())#按列求最大值索引
print(df.cummax())#返回累计最大值,nan值会被排除
print(df.describe())#汇总统计

obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj)
print(obj.describe())
