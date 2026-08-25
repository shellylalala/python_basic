"""
(1, 2, 3, ...)
和列表最大的区别在于，一旦创建好就不可修改
没有增删改，只有查
"""
# 定义有内容的元组
t1 = (28, 67, 21, 67, 11)
t2 = ('北京', '尚硅谷', '你好')
t3 = (100, True, '你好', None)
t4 = (100, True, '你好', None, (50, 60, 70))
print(type(t1), t1)  # <class 'tuple'> (28, 67, 21, 67, 11)
print(type(t2), t2)  # <class 'tuple'> ('北京', '尚硅谷', '你好')
print(type(t3), t3)  # <class 'tuple'> (100, True, '你好', None)
print(type(t4), t4)  # <class 'tuple'> (100, True, '你好', None, (50, 60, 70))

# 定义空元组
t1 = ()
t2 = tuple()
print(type(t1), t1)  # <class 'tuple'> ()
print(type(t2), t2)  # <class 'tuple'> ()

# 定义只有一个元素的元组
t1 = ('你好',)
t2 = (18,)
print(type(t1), t1)  # <class 'tuple'> ('你好',)
print(type(t2), t2)  # <class 'tuple'> (18,)


# 实际开发中的元组，不一定是我们自己定义的，比如函数的可变参数*args就是一个元组
def demo(*args):
    return sum(args)


result = demo(100, 200, 300)
print(result)  # 600
