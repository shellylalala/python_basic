"""
用来存放一组有序的字符数据，但其中的内容不可修改（只能查，不能增删改）
"""

# 支持下标查找
msg = "welcome to python"
print(msg[2])  # l
print(msg[-3])  # h

# 不可修改不可嵌套，以下均为错误案例
"""
# 字符串中的字符，不可修改
msg = 'welcome to python'
msg[0] = 'a'

# 字符串不能嵌套
msg = 'welcome to'hello' python'
msg = 'welcome to"hello" python'
# 这个是对的，转义
msg = 'welcome to\'hello\' python'
"""
