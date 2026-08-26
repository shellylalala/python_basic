class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 自定义方法
    def speak(self, msg):
        print(f"我叫{self.name}, 年龄是{self.age}, 性别是{self.gender}, 想说{msg}")


p1 = Person("张三", 18, "男")
p2 = Person("李四", 22, "女")


def speak():
    print("巴巴爸爸啦啦啦")


p1.speak = speak
print(Person.__dict__)
# Person的实例对象身上是没有speak方法的，除非去覆盖一下
print(p1.__dict__)
print(p2.__dict__)
p1.speak()
