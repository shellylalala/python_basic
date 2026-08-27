"""
定义：如果函数中又定义了函数，那么外层函数的作用域，就是内层函数的 Enclosing 作用域。
特点：
● 只有当函数“嵌套定义”时才会出现。
● 内层函数可以读取外层函数变量。
● 想修改外层变量必须使用nonlocal。
"""


def outer():
    y = 20

    def inner():
        nonlocal y
        y += 1
        print(y)

    inner()


outer()
