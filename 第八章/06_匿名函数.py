# 没有名字的函数，它无需使用def关键字去定义
# Python 中使用lambda关键字来定义『匿名函数』，格式为：lambda 参数: 表达式
#  当一个函数只用一次、只做一点点小事，使用匿名函数会更简洁。

def calculate(func, x, y):
    print(f"计算的结果为：{func(x, y)}")


calculate(lambda x, y: x + y, 10, 20)
calculate(lambda x, y: x - y, 10, 20)
calculate(lambda x, y: x * y, 10, 20)

"""
1. 只能写一行，不能写多行代码。
2. 不能写代码块（if、for、while）
3. 冒号右边必须是表达式，且只能写一个表达式。
4. 执行结果自动作为返回值。
"""

# 于是三元表达式有了用武之地
is_adult = lambda age: '成年' if age >= 18 else '未成年'
print(is_adult(18))
print(is_adult(13))
