from datetime import datetime


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    # 计数器
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.count += 1
        # 每个学生都添加student_id，格式为年份-序号，序号靠计数器实现
        self.stu_id = f"{datetime.now().year}-{Student.count:03d}"
        # 给学生添加成绩，格式为： {'数学':90, '语文':80, '英语':70}
        self.scores = {}

    # 给当前学生添加成绩
    def add_score(self, subject, score):
        # 给指定学生添加成绩，subject是学科，score是成绩
        self.scores[subject] = score

    # 计算平均分
    def calcu_avg(self):
        if self.scores:
            return sum(self.scores.values()) / len(self.scores)
        else:
            return 0

    # 魔法方法
    def __str__(self):
        return f'{self.name}({self.age}-{self.gender})，成绩：{self.scores}，平均分:{self.calcu_avg():.1f}'


class Manager:
    def __init__(self):
        self.stu_list = []

    # 添加学生
    def add_student(self):
        name = input('请输入姓名：')
        age = int(input('请输入年龄：'))
        gender = input('请输入性别：')
        stu = Student(name, age, gender)
        self.stu_list.append(stu)
        print(f'添加成功！学号是：{stu.stu_id}')

    # 删除学生
    def del_student(self):
        sid = input("请输入学号：")
        target = None
        for stu in self.stu_list:
            if stu.stu_id == sid:
                target = stu
        if target:
            self.stu_list.remove(target)
            print("删除成功！")
        else:
            print("找不到你说的学生！")

    # 展示所有学生
    def show_stu(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print("你没有学生了！")

    # 给指定学生设置成绩
    def set_score(self):
        sid = input("请输入学号：")
        for stu in self.stu_list:
            if stu.stu_id == sid:
                score_str = input("清输入成绩（学科-分数，学科-分数）：")
                if score_str:
                    # 将输入的多个成绩，按照逗号拆分，形成成绩列表
                    score_list = score_str.replace('，', ',').split(',')
                    for score in score_list:
                        subject, score = score.split('-')
                        subject = subject.strip()
                        score = float(score.strip())
                        # 调用add_score方法，添加科目，成绩
                        stu.add_score(subject, score)
                    print("添加成功！")
                else:
                    print("你也没输入啊！")
                return
        print("找不到你说的学生！")

    def run(self):
        while True:
            print('************学生管理************')
            print('1. 添加学生')
            print('2. 删除学生')
            print('3. 查看所有学生')
            print('4. 录入成绩')
            print('5. 退出')

            chocie = input('请输入操作编号：')
            if chocie == '1':
                self.add_student()
            elif chocie == '2':
                self.del_student()
            elif chocie == '3':
                self.show_stu()
            elif chocie == '4':
                self.set_score()
            elif chocie == '5':
                print('再见！')
                break
            else:
                print('输入有误！')


m1 = Manager()
m1.run()
