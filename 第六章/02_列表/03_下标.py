"""
与其他语言类似，但是有负下标，可以从后往前读
正方向0~n-1
反方向-1~-n
"""

nums = [10, 20, 30, 40, 50]

# 测试正索引
print(nums[0])  # 10
print(nums[1])  # 20
print(nums[2])  # 30
print(nums[3])  # 40
print(nums[4])  # 50

# 测试负索引
print(nums[-1])  # 50
print(nums[-2])  # 40
print(nums[-3])  # 30
print(nums[-4])  # 20
print(nums[-5])  # 10

# 定义一个嵌套列表
nums2 = [10, 20, ['你好啊', '星露谷'], 40, 50]
# 取出“尚硅谷”
print(nums2[2][1])
