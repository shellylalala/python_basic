# 1. 使用keys，获取字典中的所有的键
d1 = {'张三': 72, '李四': 60, '王五': 85}

## 返回的是dict_keys类型
result = d1.keys()
print(type(result), result)  # <class 'dict_keys'> dict_keys(['张三', '李四', '王五'])

## 可以被遍历，但不能通过下标访问
for item in result:
    print(item)

## 借助内置的list函数，可以转为list
li = list(result)
print(type(li), li)  # <class 'list'> ['张三', '李四', '王五']

# 2. values获取值
result = d1.values()
print(type(result), result)  # <class 'dict_values'> dict_values([72, 60, 85])

# 3. items获取键值对
result = d1.items()
print(type(result), result)  # <class 'dict_items'> dict_items([('张三', 72), ('李四', 60), ('王五', 85)])
