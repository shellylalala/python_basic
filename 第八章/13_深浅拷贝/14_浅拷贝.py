from copy import copy

nums1 = [10, 20, 30, 40]
nums2 = copy(nums1)
nums2[0] = 99

print(nums1)  # [10, 20, 30, 40]
print(nums2)  # [99, 20, 30, 40]

# 浅拷贝存在的问题
#   嵌套数据仍然是共享的，修改嵌套数据会互相影响

nums3 = [10, 20, 30, [40, 50]]
nums4 = copy(nums3)
nums4[3][0] = 99

print(nums3)  # [10, 20, 30, [99, 50]]
print(nums4)  # [10, 20, 30, [99, 50]]
