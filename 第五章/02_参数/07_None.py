"""
None 是一个特殊的字面量，用来表示：空值、无值、无意义
使用 None 更加中立、开放，因为它不暗示变量的类型。
1. None的类型是NoneType。
2. None出现在布尔判断中(if判断条件、while循环条件)，会被当作False来处理。
3. None不能参与任何数学运算，也不能与字符串拼接。
4. 不给函数设置返回值，那函数默认就会返回None

None出现最多的两个场景：
1. 函数中没有写return，或写了return但没有返回任何内容  。
2. 变量定义时，暂时还不知道要存放什么，可以先赋值为None。
"""

msg = None
print(type(msg))

print(bool(msg))

if not msg:
    print("msg是False")
