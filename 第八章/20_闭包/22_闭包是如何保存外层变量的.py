"""
外层变量会被保存到闭包单元（cell）中，这些cell组成一个 __closure__ 元组，保存在了inner函数上。
"""


def outer():
    num = 10

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner


f = outer()

print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(id(f.__closure__[0].cell_contents))


# inner不会保存外层outer的所有数据，只会保存inner用到的
def outer():
    num = 10
    msg = '你好啊！'
    print(msg)

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner


f = outer()
print(f.__closure__)
