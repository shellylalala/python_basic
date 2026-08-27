class AgeException(Exception):
    def __init__(self, msg):
        super().__init__("【年龄不合规】" + msg)


def age():
    age = int(input("请输入你的年龄："))
    if 18 <= age <= 120:
        print('成年')
    elif 0 <= age < 18:
        print('未成年')
    else:
        raise AgeException("你活得不像人类")


try:
    age()
except AgeException as e:
    print(f'程序异常：{e}')
