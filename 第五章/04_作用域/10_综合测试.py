# 全局作用域 与 局部作用域，以及global的使用
a = 100
b = 200


def test():
    c = "星露谷"
    d = "紫色裤衩"
    global a
    a = 300
    print('函数中的打印（a）', a)  # 300
    print('函数中的打印（b）', b)  # 200
    print('函数中的打印（c）', c)  # 星露谷
    print('函数中的打印（d）', d)  # 紫色裤衩


# test()
print('***************')


# print('全局的打印（a）', a)  # 300
# print('全局的打印（b）', b)  # 200
# print(c)  # NameError
# print(d)  # NameError


# 局部作用域 和 局部变量，会在函数调用时创建，在函数执行结束后自动销毁
def test2():
    m = 100
    m += 1
    print(f'我是test2函数中打印的m：{m}')


# test2()  # 101
# test2()  # 101
# test2()  # 101

# 全局作用域 与 全局变量，会在程序开始时创建，在程序结束后销毁
n = 100


def test3():
    global n
    n += 1
    print(f'我是test3函数中打印的n：{n}')


test3()  # 101
test3()  # 102
test3()  # 103
print(n)  # 103
