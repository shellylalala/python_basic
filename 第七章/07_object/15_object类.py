"""
object是所有类的最终祖先，所有的类，无论写与不写，都继承自object。
object提供了所有对象都会有的一组最基本方法，如果我们不去重写，Python 会自动继承并使用默认版本。
__init__(self): 在对实例对象初始化时调用
__str__(self):  print(obj)或 int(obj)时调用
__class__:      返回对象所属的类
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# 所有的类都继承了 object 类
print(issubclass(Person, object))
print(issubclass(int, object))

# 因为 object 是所有类的父类，所以 Python 中的所有对象，都间接是 object 类的实例。
p1 = Person('张三', 18, '男')
print(isinstance(p1, object))
print(isinstance(150, object))

# 所有对象都继承了 object 类所提供的：各种属性和方法，从而保证每个对象都具备统一的基本能力。
for key in object.__dict__:
    print(key)

print(p1.__dict__)
print(dir(p1))

print(p1.__str__())
print(p1)
