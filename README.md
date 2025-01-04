```markdown:5.1.1 pandas的数据结果基本功能/2、基本功能.md
# Pandas基本功能教程

## 目录
- [1. 索引操作](#1-索引操作)
- [2. 数据选取和过滤](#2-数据选取和过滤)
- [3. 算术运算和数据对齐](#3-算术运算和数据对齐)
- [4. 函数应用](#4-函数应用)
- [5. 排序和排名](#5-排序和排名)
- [6. 处理重复标签](#6-处理重复标签)

## 1. 索引操作

### 1.1 重新索引(reindex)
重新索引是Pandas中最基本的操作之一，可以改变/重排Series和DataFrame的索引。

```python
# Series重新索引
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])  # 新增的索引位置为NaN

# 填充方法
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj4 = obj3.reindex(range(6), method='ffill')  # ffill向前填充，bfill向后填充
```

### 1.2 丢弃指定轴上的项(drop)
使用drop方法可以删除Series或DataFrame指定轴上的项。

```python
# 删除行
frame.drop(['Colorado', 'Ohio'], axis=0)

# 删除列
frame.drop('two', axis=1)

# 直接修改原数据
frame.drop('two', axis=1, inplace=True)
```

## 2. 数据选取和过滤

### 2.1 基本索引方法
```python
# Series索引
obj['b']                # 通过标签访问
obj.iloc[1]            # 通过位置访问
obj[['b', 'a', 'd']]   # 多个标签索引

# DataFrame索引
frame['two']           # 选择单列
frame[['one', 'three']] # 选择多列
frame[:2]              # 选择前两行
```

### 2.2 loc和iloc选取
- `loc`: 基于标签的索引
- `iloc`: 基于位置的索引

```python
# 使用loc
frame.loc['Colorado', ['two', 'three']]  # 通过标签选择

# 使用iloc
frame.iloc[2, [3, 0, 1]]  # 通过位置选择
```

## 3. 算术运算和数据对齐

### 3.1 数据对齐
Pandas在进行运算时会自动对齐索引：
```python
# Series相加
s1 + s2  # 不同索引的运算会产生并集，缺失值为NaN

# DataFrame相加
df1 + df2  # 行列索引都会对齐
```

### 3.2 填充值处理
```python
# 使用fill_value填充缺失值
df1.add(df2, fill_value=0)  # 在计算前填充缺失值
```

## 4. 函数应用

### 4.1 apply方法
```python
# 对DataFrame应用函数
frame.apply(lambda x: x.max() - x.min())  # 默认按列计算
frame.apply(lambda x: x.max() - x.min(), axis='columns')  # 按行计算
```

### 4.2 applymap方法
```python
# 元素级别的函数应用
frame.applymap(lambda x: '%.2f' % x)  # 格式化每个元素
```

## 5. 排序和排名

### 5.1 排序
```python
# 按索引排序
frame.sort_index()  # 升序
frame.sort_index(ascending=False)  # 降序

# 按值排序
frame.sort_values(by='column')  # 按列排序
frame.sort_values(by=['A', 'B'])  # 多列排序
```

### 5.2 排名(rank)
```python
# 排名方法
series.rank()  # 默认average方法
series.rank(method='first')  # first方法
```

## 6. 处理重复标签

### 6.1 检查重复标签
```python
# 检查索引是否唯一
frame.index.is_unique

# 访问重复标签
obj['a']  # 重复标签返回Series
```

## 注意事项
1. 大多数操作默认返回新对象，使用`inplace=True`可以直接修改原对象
2. 在进行数据选取时，注意区分标签索引(loc)和位置索引(iloc)
3. 处理缺失值时可以使用填充方法
4. 排序操作可以按索引也可以按值进行

## 实用技巧
1. 使用`head()`和`tail()`快速查看数据
2. 使用`describe()`获取数据的统计信息
3. 使用`info()`查看数据基本信息
4. 使用`value_counts()`统计频率

## 参考资源
- [Pandas官方文档](https://pandas.pydata.org/docs/)
- [Pandas用户指南](https://pandas.pydata.org/docs/user_guide/index.html)
```

这个markdown文档：
1. 使用中文进行说明，便于中文用户理解
2. 包含了完整的目录导航
3. 每个部分都有代码示例
4. 增加了注意事项和实用技巧部分
5. 提供了参考资源链接
6. 使用了GitHub支持的markdown语法格式

您可以根据需要进一步调整内容或格式。
