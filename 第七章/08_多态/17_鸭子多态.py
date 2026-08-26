"""
如果一个东西看起来像鸭子，叫起来也像鸭子，那它就是鸭子
鸭子类型指一种编程风格，它并不依靠查找对象类型，来确定其是否具有正确的实现，而是直接调用或使用其方法或属性。

● 特点：不需要继承，只要传进来的对象，有对应实现就可以。
● Python 中支持“鸭子多态”。
"""


class Dog:
    def speak(self):
        print('汪汪汪！')


class Cat:
    def speak(self):
        print('喵喵喵！')


class Pig:
    def speak(self):
        print('哼哼哼！')


class Fish:
    def speak(self):
        print('咕噜噜！')


# 不再对animal的类型做限制，animal可以是任何类型，只要能调用speak方法就可以
def make_sound(animal):
    animal.speak()


# 创建实例对象
d1 = Dog()
c1 = Cat()
p1 = Pig()
f1 = Fish()

make_sound(d1)
make_sound(c1)
make_sound(p1)
make_sound(f1)
