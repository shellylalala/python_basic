"""
1. 将可能出现异常的代码放在try中，出现异常后的处理代码写在except中。
2. 如果try中的代码出现异常，那try中的后续代码不会执行，并自动跳转到except中。
3. 如果try中的代码没有异常，那except中的代码就不会执行。
4. 无论是否发生异常，try-except后面的代码都会继续执行。
5. 直接写except捕获到Python中所有的异常 ———— 实际开发中不推荐这样做
"""
print("欢迎使用本程序")
try:
    a = int(input("请输入被除数："))
    b = int(input("请输入除数："))
    res = a / b
    print(f"{a} / {b} = {res}")
except:
    print("抱歉，程序出现了异常")
finally:
    print("程序执行结束")
