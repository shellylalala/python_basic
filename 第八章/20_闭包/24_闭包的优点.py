"""
1. 可以“记住”状态：不用全局变量，也不用写类，就能在多次调用之间保存数据。
2. 可以做“配置过的函数”：先传一部分参数，把环境固定住，得到一个定制版函数。
3. 可以实现简单的“数据隐藏”：外层变量对外不可见，只能通过内层函数访问。
4. 是装饰器（decorator）等高级用法的基础。
"""


def outer(char, n):
    def inner(msg):
        print(char * n + msg + char * n)

    return inner


show1 = outer("-", 5)
show1("这是一个闭包")
show1("这也是一个闭包")

show2 = outer("@", 8)
show2("这还是闭包")
show2("这难道就不是闭包了吗")
