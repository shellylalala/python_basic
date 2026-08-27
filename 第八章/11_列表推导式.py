"""
● 概念：用一条简洁语句，从可迭代对象中，生成新列表的语法结构。
● 语法格式：[ 表达式 for 变量 in 可迭代对象 ]
"""

# 需求：让nums列表中所有的元素，都变为原来的2倍

## 方法一
nums = [10, 20, 30, 40]
result = map(lambda n: n * 2, nums)
print(list(result))

## 方法二
nums = [10, 20, 30, 40]
result = []
for n in nums:
    result.append(n * 2)
print(result)

## 方法三
nums = [10, 20, 30, 40]
result = [n * 2 for n in nums]
### 带有条件的推导式
# result = [n * 2 for n in nums if n > 20]
print(result)

# 字典推导式
names = ['张三', '李四', '王五']
scores = [60, 70, 80]
result = {names[i]: scores[i] for i in range(len(names))}
print(result)

# 集合推导式
names = ['张三', '李四', '王五']
result = {n + "！" for n in names}
print(result)

names = ['张三', '李四', '王五']
# 注意：Python中没有元组推导式，下面这种写法叫：生成器
result = (n + '！' for n in names)
print(result)
