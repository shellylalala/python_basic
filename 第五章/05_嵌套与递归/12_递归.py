"""
递归调用：函数自己调用自己的一种操作
递归必须要具备终止条件（不能无限的一直调用，总得有停下来的时候。）
"""


# 使用递归实现一个数的阶乘
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


print(factorial(5))
