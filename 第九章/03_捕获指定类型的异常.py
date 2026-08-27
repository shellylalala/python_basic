print("欢迎使用本程序")
try:
    a = int(input("请输入被除数："))
    b = int(input("请输入除数："))
    res = a / b
    print(f"{a} / {b} = {res}")
except ZeroDivisionError:
    print("除数为0，无法执行")
except ValueError:
    print("抱歉，您必须输入数字")
except:
    print("反正你有错！")

"""
多个except的话，从上往下依次匹配，匹配成功后不再向下匹配
"""
