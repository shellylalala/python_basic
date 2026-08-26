"""
在类中直接写赋值语句（例如：a = 100），就会在类身上添加一个a属性，值为100
此时的a就是『类属性』，它属于类本身，由类所拥有，
并且该类创建出来的所有实例对象，都能去访问a属性。

特点：
1. 所有实例访问的，都是同一个类属性，所以类属性通常用于：存放公共数据。
2. 类属性即可以通过『类』访问，也可以『实例』访问。
"""


class Person:
    MAX_AGE = 120
    planet = "地球"

    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender

        if age <= self.MAX_AGE:
            self.age = age
        else:
            self.age = self.MAX_AGE


# 实例对象身上是没有类属性的
p1 = Person('张三', 122, '男')
p2 = Person('李四', 115, '女')

print(p1.age)  # 120
print(p2.age)  # 115

# 进行实例.属性名 = xxx操作时，只会对实例自身的属性起作用（有则修改，无则添加）！
p1.planet = "火星"
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
print(p1.planet)
print(p2.planet)
