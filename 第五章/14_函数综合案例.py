def calc_total(n):
    """
    计算总运动量（个）
    :param n: 每一天的运动量
    :return: 总运动量
    """
    return sum(n)


def calc_avg(total, days=7):
    """
    计算平均值
    :param total: 总运动量
    :param days: 运动的天数
    :return: 平均值
    """
    return total / days


def check_success(total, goal=120):
    """
    判断是否运动成功
    :param total: 总运动量
    :param goal: 成功数量（默认120）
    :return: 成功或者失败
    """
    if total >= goal:
        return '✅恭喜！挑战成功！'
    else:
        return '❌抱歉！挑战失败！'


def main(title, duration, goal):
    """
    主函数，用于开始一场挑战赛
    :param title: 比赛标题
    :param duration: 比赛持续天数
    :param goal: 目标运动量
    :return: None
    """
    print(f'【{title}】【{duration}天】✊️挑战赛（请输入每天的数量）')
    daily_amount = []
    for i in range(duration):
        amount = int(input(f'请输入第{i + 1}天的运动量：'))
        daily_amount.append(amount)

    total = calc_total(daily_amount)

    avg = calc_avg(total, duration)

    result = check_success(total, goal)

    print('\n======挑战结果======')
    print(f'总运动量：{total} 个')
    print(f'平均每天：{avg:.2f} 个')
    print(f'目标数量：{goal} 个')
    print(result)


if __name__ == '__main__':
    main("俯卧撑", 3, 60)
