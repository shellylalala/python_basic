"""
● reduce函数：将一组数据不断“合并”，最终归并成一个结果。
● 语法格式：reduce(合并函数, 可迭代对象, 初始值)。
备注：reduce函数需要从functools模块中引入才能使用。
"""

from functools import reduce

print("-----数值统计-----")
# 数值统计
nums = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, nums, 10)
print(result)

print("-----字符串拼接-----")
# 字符串拼接
str_list = ['ab', 'cd', 'ef']
result = reduce(lambda a, b: a + b, str_list)
print(result)
