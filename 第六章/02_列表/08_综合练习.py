print("请输入学生成绩(0~100)，输入“停止”则停止录入")
score_list = []

while True:
    score = input("📝请输入成绩：")
    if score == "结束":
        break
    elif not score.isdigit():
        print("❌请输入数字成绩！")
        continue

    score = int(score)
    if score < 0 or score > 100:
        print("❌成绩必须在0~100之间！")
        continue

    score_list.append(score)

if len(score_list) > 0:
    # 统计平均分
    avg_score = sum(score_list) / len(score_list)
    # 合格人数
    pass_count = 0
    # 优秀刃叔
    excellent_count = 0
    for score in score_list:
        if score >= 60:
            pass_count += 1
        if score >= 90:
            excellent_count += 1
    # 合格率
    pass_rate = pass_count / len(score_list) * 100
    # 优秀率
    excellent_rate = excellent_count / len(score_list) * 100
    # 打印信息
    print('********⬇️统计信息如下⬇️********')
    print(f'🧑‍🎓总人数为：{len(score_list)}')
    print(f'🔺最高分为：{max(score_list)}')
    print(f'🔻最低分为：{min(score_list)}')
    print(f'✅合格人数：{pass_count}人')
    print(f'📈合格率为：{pass_rate:.1f}%')
    print(f'🏆优秀人数：{excellent_count}人')
    print(f'📈优秀率为：{excellent_rate:.1f}%')
    print(f'📊平均分数：{avg_score:.1f}')
else:
    print("您未录入任何成绩！")
