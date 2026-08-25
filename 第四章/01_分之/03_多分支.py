"""
if 判断条件1:
    条件1【成立】时执行的代码
elif 判断条件2:
    条件2【成立】时执行的代码
elif 判断条件3:
    条件3【成立】时执行的代码
else:  # else如不需要可以省略
    上述所有条件都不成立时执行的代码
"""
age = int(input("请输入你的年龄："))
if age <= 7:
    print("先上幼儿园吧你")
elif age <= 13:
    print("先上小学吧你")
elif age <= 16:
    print("先上初中吧你")
elif age <= 18:
    print("先上高中吧你")
else:
    print("是时候来一盘紧张刺激的星露谷了")
