"""
continue：跳过本次循环剩余语句，直接进入下一次循环判断
"""
# 测试continue
"""
每次循环都没有睡觉
"""
# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     continue
#     print('睡觉')

"""
第二天没有睡觉
"""
# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     if day == 2:
#         continue
#     print('睡觉')

"""

"""
# for day in range(1, 5):
#     if day == 2:
#         continue
#     print(f'********第{day}天********')
#     print('吃饭')
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     for item in range(1, 3):
#         print(f'面包{item}')
#         continue
#         print(f'牛奶{item}')
#     print('睡觉')

for day in range(1, 5):
    print(f'********第{day}天********')
    print('吃饭')
    for item in range(1, 3):
        print(f'面包{item}')
        if day == 4 and item == 2:
            continue
        print(f'牛奶{item}')
    print('睡觉')
