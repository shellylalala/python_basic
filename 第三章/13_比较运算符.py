# ==
a = 5
b = 7
c = "5"
result = a == b
print(result) # False

# !=
a = 5
b = 7
c = "5"
result = a != b
print(result)  # True

# 使用>判断左侧是否大于右侧
a = 9
b = 7
c = '5'
result = a > b
print(result)

# 使用<判断左侧是否小于右侧
a = 3
b = 7
c = '5'
result = a < b
print(result)

# 使用>=判断左侧是否大于等于右侧
a = 6
b = 7
c = '5'
result = a >= b
print(result)

# 使用<=判断左侧是否小于等于右侧
a = 9
b = 7
c = '5'
result = a <= b
print(result)

# 以上这些比较运算符，同样适用于字符串
# 字符串进行比较时，是依次比较每个字符的 Unicode 编码。
msg1 = 'abc'
msg2 = 'abc666'
print(msg1 == msg2)

msg1 = 'abc'
msg2 = 'abc'
print(msg1 != msg2)