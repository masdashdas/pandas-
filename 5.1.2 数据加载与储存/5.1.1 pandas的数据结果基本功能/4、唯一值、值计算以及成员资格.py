import pandas as pd
import numpy as np

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
print(obj)
print(obj.unique())#返回唯一值
print(obj.value_counts())#返回唯一值及其频率
print(obj.values)
print(pd.value_counts(obj.values, sort=False))#返回唯一值及其频率，不排序，默认sort=True，排序
print(pd.value_counts(obj.values, sort=True))

#isin用于判断元素是否在序列中
print(obj)
mask = obj.isin(['b', 'c'])
print(mask)
print(obj[mask])

#与isin类似Index.get_indexer()方法，返回索引值
to_match = pd.Series(['c', 'a', 'b', 'b', 'c','c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
print(pd.Index(unique_vals).get_indexer(to_match))

data= pd.DataFrame({'Qu1': [1, 3, 4, 3, 4], 'Qu2': [2, 3, 1, 2, 3], 'Qu3': [1, 5, 2, 4, 4]})
print(pd)
result = data.apply(pd.value_counts).fillna(0)
print(result)
