"""
# 定义一个类（类名通常用大驼峰写法）
class 类名:
    # 当一个函数被定义在类中时，它就被称为“方法”。
    # __init__方法又叫：初始化方法，它主要用来给当前实例对象添加属性。
    # __init__方法收到的参数是：当前正在创建的实例对象、其他自定义参数。
    # 当我们后期编写代码，对类进行实例化的时候，Python就会自动调用__init__方法，去完成对实例的初始化。
    def __init__(self, 参数1, 参数2, 参数3):
        # 通过self给当前实例添加属性，语法格式为：self.属性名 = 属性值
        self.属性名 = 参数1
        self.属性名 = 参数2
        self.属性名 = 参数3
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# 创建实例对象
p1 = Person("张三", 18, "男")
print(p1.name)  # 张三
p2 = Person("李四", 22, "女")

# 通过实例的“点”语法，可以『访问』或『修改』实例的属性。
p1.name = "王五"
print(p1.name)  # 王五

# 通过实例.__dict__ 的方式，可以查看实例身上的所有属性。
print(p1.__dict__)  # {'name': '王五', 'age': 18, 'gender': '男'}

# 通过type() 函数，可以查看某个实例对象，是由哪个类创建出来的
print(type(p1))  # <class '__main__.Person'>
