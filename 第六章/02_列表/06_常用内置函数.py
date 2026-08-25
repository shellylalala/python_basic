# Python 中有一些内置函数，可以用来处理列表

# 1. sorted(数据容器, reverse=布尔值)
# 对容器排序（从小到大，不会改变原容器），返回值：经过排序的新容器
# 第一手数字则按照数字大小排序，都是字符串按照Unicode排序，不能混
nums = [23, 11, 32, 30, 17]
result = sorted(nums, reverse=True)
print(nums)  # [23, 11, 32, 30, 17]
print(result)  # [32, 30, 23, 17, 11]

# 2. len(数据容器)
# 获取容器中元素的个数，返回值：元素个数。
nums = [10, 20, 10, 30, 10, 40, [50, 60, 70]]
result = len(nums)
print(result)  # 7

# 3.max(数据容器)
# 返回容器中或多个值中的最大值，返回值：容器中的最大值
nums = [23, 11, 32, 30, 17]
result = max(nums)
print(nums)  # [23, 11, 32, 30, 17]
print(result)  # 32

msg_list = ['老乡', '星露谷', '你好']
result = max(msg_list)
print(msg_list)  # ['老乡', '星露谷', '你好']
print(result)  # 老乡

# 4. min(数据容器)
# 返回容器中或多个值中的最小值，返回值：容器中的最小值
# 和max一样的用法
nums = [23, 11, 32, 30, 17]
result = min(nums)
print(result)  # 11

# 5. sum(数据容器)
# 对容器中所有元素求和（只能是数值类型），返回值：所有元素的和
nums = [23, 11, 32, 30, 17]
result = sum(nums)
print(result)  # 113
