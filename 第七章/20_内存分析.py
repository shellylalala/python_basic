"""
内存分为两个部分：栈内存、堆内存；变量在栈内存中，对象在堆内存中。
"""

"""
# Python 中变量里保存的不是存数据，而是指向堆中对象的引用（内存地址）
a = 666
print(id(a))

# Python 中常见的不可变对象有：int 、float 、bool 、str 、tuple 、frozenset 、None。
# Python 中常见的可变对象有：list 、dict 、set 、自定义类的实例对象
b = a
print(id(b))

a = 888
print(id(a))
print(id(b))

# 此后，666的内存被回收了
del b
print(id(a))
b = a
print(id(b))
"""

"""
# 可变对象：修改内容不改变地址
stu_list = ["张三", "李四", "王五"]
print(id(stu_list))
stu_list[0] = "赵六"
print(id(stu_list))
"""


# 自定义类对象的内存表示
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is {self.age} years old")


p1 = Person("张三", 18)
print(id(p1))
print(id(p1.speak))
p2 = Person("李四", 18)
print(id(p2))
print(id(p2.speak))
