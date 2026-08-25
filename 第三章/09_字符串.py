# 字符串的格式化输出
name = "张三"
gender = "男"
age = 22
weight = 65.2

# 加号拼接
print('我叫' + name + '，我是' + gender + '生')

# 占位符
print('我叫%s，我是%s生，我体重是%f，年龄是%d' % (name, gender, weight, age))
# 控制位数
print('我叫%s，我是%s生，我体重是%-9.3f，年龄是%d' % (name, gender, weight, age))

# f-string
print(f'我叫{name}，我是{gender}生，我体重是{weight}，年龄是{age}')

# 转义字符
# \+符号，很熟了，不赘述
