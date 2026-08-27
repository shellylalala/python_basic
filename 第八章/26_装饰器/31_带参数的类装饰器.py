class SayHello:
    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'你好，我要开始{self.msg}计算了')
            return func(*args, **kwargs)

        return wrapper


@SayHello('加法')
def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res


result = add(1, 2)
print(result)

