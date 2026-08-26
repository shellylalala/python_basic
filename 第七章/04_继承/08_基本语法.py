"""
概念：指一个类可以继承另一个类的属性和方法
作用：实现代码的复用和扩展，避免编写重复的代码
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f"我叫{self.name}，我今年{self.age}岁了，我是{self.gender}生，我想说{msg}。")


class Student(Person):
    def __init__(self, name, age, gender, s_id, grade):
        # 继承父类属性
        super().__init__(name, age, gender)

        # 或者这么写
        # Person.__init__(self, name, age, gender)

        # 子类独有的属性
        self.s_id = s_id
        self.grade = grade

    def study(self):
        print(f"我叫{self.name}，我正在努力学习，争做{self.grade}的第一")


s1 = Student("李华", 16, "男", "20260101", "初三")
# print(s1.__dict__)
# print(type(s1))  # Student

# s1.speak("你好")

# print(s1.__dict__)

# 查找study方法的过程：1.实例自身(s1) => 2.Student类 => 3.Person类
s1.study()

"""
几个说明：
1. 定义类时，在类名后写圆括号()，并填入另一个类名，表示该类继承自另一个类。
2. 在子类中，可以直接使用父类中定义的：属性、方法，也可以定义自己独有的内容。
3. super().__init__()的作用：调用父类的初始化方法。
"""
