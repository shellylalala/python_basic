"""
如果子类中定义了与父类同名的方法，则会子类会“覆盖”父类中的方法，又称：“重写”。
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
        super().__init__(name, age, gender)
        self.s_id = s_id
        self.grade = grade

    # 方法重写：当子类中定义了一个与父类中相同的方法，那么子类中的方法就会“覆盖”父类的方法
    def speak(self, msg):
        super().speak(msg)
        print(f'我是学生，我的学号是{self.s_id}，我正在读{self.grade}，我想说：{msg}')


s1 = Student('李华', 12, '男', '2025001', '初二')
s1.speak('好好学习')
