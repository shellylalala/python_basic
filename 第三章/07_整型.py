"""
所谓整型就是没有小数点的数字， Python 中的整型，可以是任意大小的整数，包括负整数
"""

import sys

# 无上限整型最大值
sys.set_int_max_str_digits(0)

# 分隔符，使数字分组，更便于读取
num1 = 100_000_000
print(num1)

num2 = 9 ** 999999
print(num2)
