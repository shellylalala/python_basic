"""
1. 理解成本较高：对初学者不太友好，滥用会让代码难读。
2. 如果闭包里引用了很大的对象，又长期不释放，可能会增加内存占用。
3. 很多场景下，其实用【类 + 实例属性】会更清晰，闭包不一定是最优解。
"""


class MyClass:
    def __init__(self, char, num):
        self.char = char
        self.num = num

    def show_msg(self, msg):
        print(self.char * self.num + msg + self.char * self.num)


show1 = MyClass("-", 5)
show1.show_msg("hello")
show1.show_msg("world")
