"""
创建一个新的外层容器，同时对内部所有【可变对象】进行递归复制（不可变对象不复制，继续引用）
"""
from copy import deepcopy, copy

nums1 = [10, 20, 30, [40, 50]]
nums2 = deepcopy(nums1)
nums2[3][0] = 99

print(nums1)  # [10, 20, 30, [40, 50]]
print(nums2)  # [10, 20, 30, [99, 50]]

"""
特点：
1. 深拷贝可以彻底消除数据之间的相互影响
2. 深拷贝遇到不可变对象不会复制，会直接引用

注意点：
1. 深拷贝只复制可变对象，不可变对象直接引用
2. 元组中若只包含不可变对象，则深拷贝没有效果
"""
a = 666
# a是不可变对象，即便调用deepcopy也不会深拷贝，会直接引用
b = deepcopy(a)

print(id(a))
print(id(b))

nums1 = (10, 20, 30, [40, 50])
# nums1元组中只包含不可变对象，即便调用deepcopy也不会深拷贝
nums2 = deepcopy(nums1)

print(id(nums1))
print(id(nums2))
