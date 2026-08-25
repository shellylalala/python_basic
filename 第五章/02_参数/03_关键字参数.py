# 关键字参数：函数调用时通过形参名 = 值的形式传递的参数，就是关键字参数

# 定义函数
def greet(name, gender, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')


# 调用函数（使用关键字参数）
# greet(name='张三', gender='男', age=18, height=172)
# greet(height=172, age=18, gender='男', name='张三')

# 位置参数』和『关键字参数』可以混用，但『位置参数』必须写在『关键字参数』之前！
greet('张三', '男', height=172, age=18)