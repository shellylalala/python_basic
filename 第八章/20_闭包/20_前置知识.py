# 1. 局部作用域的生命周期
"""
● 每次调用函数时，都会创建一个新的局部作用域。
● 函数执行完毕后，该作用域就会被销毁，其中的局部变量，也会随之释放。
"""


def outer():
    num = 10
    num += 1
    print(num)


outer()
outer()
outer()

print("-----分割-----")

# 2. 内层函数访问外层变量
"""
● 【内层函数】可以访问到【外层函数】作用域中的变量。
● 访问外层变量不用nonlocal，修改外层变量时要使用nonlocal。
"""


def outer():
    num = 10

    def inner():
        print(num)

    return inner


f = outer()
f()
