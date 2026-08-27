# 1. 每次获得一个新闭包，互不影响（闭包之间是互相独立的）。

def outer():
    num = 10

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner


f1 = outer()
f1()  # 11
f1()  # 12
f1()  # 13
print('*****************')
f2 = outer()
f2()  # 11

print('*****************')


# 2. 外层变量为可变对象时仍互不影响
def outer():
    nums = []

    def inner(value):
        nums.append(value)
        print(nums)

    return inner


# 每次调用 outer() 都创建一个新的 nums
f1 = outer()
f1(10)
f1(20)
f1(30)
print('**********************')
f2 = outer()
f2(666)
