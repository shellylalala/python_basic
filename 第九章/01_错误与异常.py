# 1. 错误
# 代码本身有语法错误，解释器无法执行，无法通过异常处理机制解决
# age = 18
# if age >= 18          # SyntaxError: expected ':'
#     print('成年人')

# 2. 异常
# 代码在语法上没问题，但执行过程中出现了问题可以通过异常处理机制解决

print("-----常见的异常-----")

# 1. ZeroDivisionError: 除数为0
# num1 = 100
# num2 = 0
# result = num1 / num2

# 2. TypeError: 操作的数据类型不正确或者不兼容
# result = '10' + 5

# 3. AttributeError: 对象没有指定的属性或方法
## 演示一
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p1 = Person('张三', 18)
# print(p1.name)
# print(p1.age)
# print(p1.gender)

# 演示2
# nums = [10, 20, 30]
# nums.add(40)

# 4.IndexError: 当索引超出范围（索引越界）时触发。
# nums = [10, 20, 30, 40]
# print(nums[4])

# 5.NameError: 当使用了不存在的变量时触发。
# print(school)

# 6.KeyError: 当访问字典中不存在的 key 时触发。
# person = {'name':'张三', 'age':18}
# print(person['gender'])

# 7.ValueError：当值不合法，但类型正确时触发。
# int('hello')