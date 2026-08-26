"""
同样支持for和while
"""
msg = 'welcome to python'
# while循环遍历
index = 0
while index < len(msg):
    print(msg[index])
    index += 1

# for循环遍历
for item in msg:
    print(item)
