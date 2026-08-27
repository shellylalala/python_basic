"""
map函数：对一组数据中的每一个元素，统一执行某种操作（加工），并生成一组新数据。
语法格式：map(操作函数, 可迭代对象)
"""

print("-----统一数据处理-----")

# 统一数据处理
nums = [10, 20, 30, 40]
result = map(lambda x: x * 2, nums)
print(list(result))
print(nums)

print("-----字符串转换-----")

# 字符串转换
names = ("python", "java", "c++")
result = map(lambda str: str.upper(), names)
print(tuple(result))
print(names)

print("-----类型转换-----")

# 类型转换
str_nums = {"1", "2", "3"}
result = map(lambda str: int(str), str_nums)
print(set(result))
print(str_nums)

print("---------------")
# 注意点：
# 1.延迟执行：map 不会立刻计算，只有在“需要结果”时才执行计算。
# 2.返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”。
# 3.map不会影响元素数量。


nums = [10, 20, 30, 40]
result = list(map(lambda x: x * 2, nums))
print(result)
print(result)
print(result)
print(result)
