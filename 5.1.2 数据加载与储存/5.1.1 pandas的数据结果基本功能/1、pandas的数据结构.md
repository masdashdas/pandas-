### Pandas 基础知识复习

#### 1. Series 创建与基本操作
- **创建 Series**: 
  ```python
  obj = pd.Series([4, 5, 6, 4, 1, 4])
  ```

- **获取值与索引**:
  ```python
  print(obj.values)  # 获取值
  print(obj.index)   # 获取索引
  ```

- **自定义索引**:
  ```python
  obj2 = pd.Series([4, 5, -7, 3], index=['d', 'b', 'a', 'c'])
  ```

- **通过索引获取值与修改值**:
  ```python
  print(obj2['a'])  # 获取值
  obj2['d'] = 6     # 修改值
  ```

- **条件筛选与修改**:
  ```python
  obj2[obj2 > 0] = 0  # 通过条件筛选修改值
  ```

#### 2. 数据缺失处理
- **判断空值**:
  ```python
  print(pd.isnull(obj4))  # 判断是否为空
  print(pd.notnull(obj4))  # 判断是否非空
  ```

#### 3. DataFrame 创建与基本操作
- **创建 DataFrame**:
  ```python
  data = {'state': ['Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002], 'pop': [1.5, 2.4, 2.9]}
  frame = pd.DataFrame(data)
  ```

- **更改索引与获取列数据**:
  ```python
  frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'])
  print(frame2['state'])  # 通过列名获取数据
  ```

- **行列选择**:
  ```python
  frame2.loc['one']  # 通过标签获取行
  frame2.iloc[1]     # 通过位置获取行
  ```

#### 4. DataFrame 的列和索引操作
- **修改与创建新列**:
  ```python
  frame2['debt'] = 16.5  # 添加新列
  frame2['eastern'] = frame2.state == 'Ohio'  # 布尔值赋值
  ```

- **删除列**:
  ```python
  del frame2['eastern']  # 删除列
  ```

#### 5. 索引对象
- **Index 对象的特性**:
  ```python
  labels = pd.Index(np.arange(3))
  ```

- **索引不可变性**:
  ```python
  obj.index = ['d', 'b', 'a']  # 尝试修改索引
  ```

- **重复索引**:
  ```python
  dup_labels = pd.Index(['foo', 'bar', 'baz', 'foo'])
  obj3 = pd.Series(np.random.randn(4), index=dup_labels)
  ```

### 复习小贴士
- **理解数据结构**: 重点掌握 Series 和 DataFrame 的结构及常用操作。
- **多做练习**: 通过实际编写代码来巩固对 pandas 函数的理解。
- **关注数据处理**: 特别是空值处理和索引管理，是日常数据分析的重要部分。

