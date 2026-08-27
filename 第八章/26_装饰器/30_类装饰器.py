"""
1. 包含__call__方法的类，就是类装饰器。
2. 像调用函数一样，去调用类装饰器的实例对象，就会触发__call__方法的调用。
3. __call__方法通常接收一个函数作为参数，并且会返回一个新函数。
"""


class SayHello:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("你好，我要开始计算了")
            return func(*args, **kwargs)

        return wrapper


@SayHello()
def add(a, b):
    res = a + b
    print(f'{a}和{b}相加的结果是{res}')
    return res


say = SayHello()
add = say(add)

result = add(1, 2)
print(result)
