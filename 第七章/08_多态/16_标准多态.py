"""
多态的定义：不同的对象调使用同一个方法名调用方法时，会表现出不同的行为。

标准多态：
● 基于继承实现多态，又叫：『传统多态』或『标准多态』。
● 常见于Java、C++ 这样的强类型语言中，Python支持『标准多态』。
"""


# 标准多态：
class Animal:
    def speak(self):
        print('动物正在发出声音')


class Dog(Animal):
    def speak(self):
        print('汪汪汪！')


class Cat(Animal):
    def speak(self):
        print('喵喵喵！')


# 注意Pig类没有继承Animal类
class Pig:
    def speak(self):
        print('哼哼哼！')


# make_sound函数要求：传入的对象，必须是 Animal 类型（或其子类型），才能保证可以调用到speak方法
def make_sound(animal: Animal):
    animal.speak()


# 创建实例对象
a1 = Animal()
d1 = Dog()
c1 = Cat()

# 多态的体现：同一函数，不同对象 → 不同行为
make_sound(a1)  # 动物正在发出声音
make_sound(d1)  # 汪汪汪！
make_sound(c1)  # 喵喵喵！

# 按标准多态规则：Pig 没有继承 Animal，类型不匹配（会出现类型警告）
p1 = Pig()
make_sound(p1)  # 在其它语言中会报错，虽然 Python 中能运行，但这不属于标准多态
