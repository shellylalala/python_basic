"""
● 闭包 = 内层函数 + 被内层函数引用的外层变量。
● 产生闭包的三个条件如下：
1. 必须有函数嵌套
2. 内层函数使用了外层函数的变量
3. 外层函数返回内层函数
"""


def outer():
    num = 10

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner


f = outer()
f()  # 11
f()  # 12
f()  # 13
