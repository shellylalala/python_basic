"""
在面向对象编程中，我们会把一些内部数据保护起来，但同时还想提供一个“安全的通道”让外部访问。这时候我们就用到：
● getter：读取属性的方法
● setter：修改属性的方法
在 Python 中：通过@property和@xxx.setter语法，把普通方法变成像属性一样使用的方法。
"""


class Person:
    def __init__(self, name, age, idcard):
        # 公有属性：当前类内部、子类内部、类外部，可都可访问
        self.name = name
        # 受保护属性：当前类内部、子类内部，可以访问
        self._age = age
        # 私有属性：仅能在当前类内部访问
        self.__idcard = idcard

    # 注册 age 属性的 getter 方法：当访问 Person 实例的 age 属性时，age方法会自动调用
    @property
    def age(self):
        return self._age

    # 注册 age 属性的 setter 方法：当给 Person 实例的 age 属性赋值时，age方法会自动调用
    @age.setter
    def age(self, value):
        if value <= 120:
            self._age = value
        else:
            self._age = 120

    # 注册 idcard 属性的 getter 方法：当访问 Person 实例的 idcard 属性时，会自动调用此方法
    @property
    def idcard(self):
        return self.__idcard[:6] + '********' + self.__idcard[-4:]

    # 注册 idcard 属性的 setter 方法，当 idcard 被修改时调用，内部会禁止修改身份证号并给出提示。
    @idcard.setter
    def idcard(self, value):
        print("抱歉，身份证号不允许随意修改，如有特殊需求，请联系管理员！")


p1 = Person('张三', 18, '110101199001011234')
# print(p1.age)
# print(p1.idcard)

p1._age = 18
print(p1.age)

p1.idcard = "asd"
