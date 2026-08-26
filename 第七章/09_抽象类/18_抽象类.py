"""
● 概念：抽象类（Abstract Class） 是一种 不能被直接实例化 的类，通常作为“规范”，让子类去继承并实现其中定义的抽象方法，本身只定义规范，不需要提供完整实现。
● 例如：动物会叫、飞行器会飞、支付方式会支付。
"""
from abc import ABC, abstractmethod


class MustRun(ABC):
    @abstractmethod
    def run(self):
        pass


class Person(MustRun):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print(f'我叫{self.name}，我在努力的奔跑！')


p1 = Person('张三', 18, '男')
p1.run()
