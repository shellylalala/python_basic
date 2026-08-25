"""
break：立即终止循环，不再执行后续循环
"""

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     break
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     if day == 2:
#         break
#     print('睡觉')

# for day in range(1, 5):
#     if day == 2:
#         break
#     print(f'********第{day}天********')
#     print('吃饭')
#     print('睡觉')

for day in range(1, 5):
    print(f'********第{day}天********')
    print('吃饭')
    for item in range(1, 3):
        print(f'面包{item}')
        if day == 4 and item == 2:
            break
        print(f'牛奶{item}')
    print('睡觉')
