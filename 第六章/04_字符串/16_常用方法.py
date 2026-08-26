# 1. index
msg = 'welcome to python'
result = msg.index("o")
print(result)  # 4

# 2. split
## 按照指定分割，返回list
result = msg.split("o")
print(result)  # ['welc', 'me t', ' pyth', 'n']

# 3. replace
## 将字符串中的某个片段替换为目标
result = msg.replace("o", "O")
print(result)  # welcOme tO pythOn

# 4. count
## 统计指定字符的出现次数
result = msg.count("o")
print(result)  # 3

# 5. strip
## 从字符串两端开始删除，直到遇到第一个不在字符串中的字符就停下
result = msg.strip("w")
print(result)  # elcome to python
