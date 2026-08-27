# 需求描述：
# 在不修改add函数的前提下，给add函数增加一些额外的功能，例如：计算前打印一句欢迎语。

# 1. 定义装饰器函数
def say_hello(func):
    def wrapper(*args, **kwargs):
        print("你好，我要开始计算了")
        return func(*args, **kwargs)

    return wrapper


"""
定义装饰器核心规则：
1. 接收被装饰的函数、同时返回新函数（wrapper）
2. 装饰器“吐出来”的是 wrapper 函数，以后别人调用的也是 wrapper 函数。
3. 为了保证参数的兼容性，wrapper 函数要通过 *args 和 **kwargs 接收参数。
4. wrapper 函数中主要做的是：调用原函数（被装饰的函数）、执行其它逻辑，但要记得将原函数的返回值 return 出去。
"""


# 3. 使用语法糖
@say_hello("加法")
def add(x, y, z):
    res = x + y + z
    print(f'{x}和{y}和{z}相加的结果是：{res}')
    return res


# 2. 使用函数装饰器
# 调用say_hello装饰器，对add函数进行装饰，并得到装饰后的新函数
add = say_hello(add)

result = add(10, 20, 30)
print(result)

"""
上述代码的执行流程：
1. @say_hello 会自动执行： add = say_hello(add)。
2. 以后调用 add()时，真正执行的是wrapper()。
"""
