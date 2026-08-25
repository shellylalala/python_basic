"""
使用return关键字可以设置函数的返回值，return的作用有两个，分别是：
1. 结束函数的运行。
2. 把return后面的值，作为函数的返回值。
"""


# 定义函数
def add(n1, n2):
    print(f'我收到了：{n1}、{n2}，二者相加是：{n1 + n2}')
    print('add函数执行完毕了')
    return n1 + n2


# 调用函数
result = add(100, 200)
print(result)

# print函数是没有返回值的
res = print('hello')
print(res)
