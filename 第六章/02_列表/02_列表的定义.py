"""
[a, b, c, d]
"""
# 有内容的列表
list1 = [34, 56, 21, 56, 11]
list2 = ['北京', '尚硅谷', '你好啊']
list3 = [23, '尚硅谷', True, None]
list4 = [23, '尚硅谷', True, None, [100, 200, 300]]  # list4 是一个嵌套列表

# 定义空列表（列表中的数据，后期会通过特定写法填充）
list5 = []
list6 = list()

print(list1, type(list1))  # [34, 56, 21, 56, 11] <class 'list'>
print(list2, type(list2))  # ['北京', '尚硅谷', '你好啊'] <class 'list'>
print(list3, type(list3))  # [23, '尚硅谷', True, None] <class 'list'>
print(list4, type(list4))  # [23, '尚硅谷', True, None, [100, 200, 300]] <class 'list'>
print(list5, type(list5))  # [] <class 'list'>
print(list6, type(list6))  # [] <class 'list'>
