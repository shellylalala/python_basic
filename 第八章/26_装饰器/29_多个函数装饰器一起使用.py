"""
多个函数装饰器一起使用
核心：注意装饰顺序，距离函数最近的装饰器，会先工作。
例如下面代码：test2先装饰，test1再装饰。
"""


def test1(func):
    print('我是test1装饰器')

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('test1追加的逻辑')
        return res

    return wrapper


def test2(func):
    print('我是test2装饰器')

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('test2追加的逻辑')
        return res

    return wrapper


@test1
@test2
def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res


result = add(10, 20)
print(result)
