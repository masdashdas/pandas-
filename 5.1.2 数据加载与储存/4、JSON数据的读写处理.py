import json
import pandas as pd
import numpy as np  

obj = """{"name":"Wes","plasces_lived":["United States","Spain","Germany"],"pet":null,"siblings":[{"name":"Scott","age":25,"pets":["dog","cat"]},{"name":"Katie","age":35,"pets":["dog"]}]}"""

result = json.loads(obj)
print(result)

asjson = json.dumps(result)
print(asjson)
print(type(asjson))

data = pd.read_json('5.1.2 数据加载与储存\data\example.json')
print(data)

print(data.to_json())#orient默认为split 输出json对象

print(data.to_json(orient='records'))#输出json数组

