from area import *
from course import *
from grade import *
from student import *
from teacher import *


class SchoolManageIT:
    new_area = Area("North")  # 创建南北校区 #
    old_area = Area("South")

    chinese = Course("Chinese", 50)  # 创建课程 #
    math = Course("Math", 125)
    english = Course("English", 25)
    physics = Course("Physics", 75)
    science = Course("Science", 50)
    chemistry = Course("Chemistry", 100)
    geography = Course("Geography", 50)

    grade_1 = Grade("Grade 1")  # 创建班级 #
    grade_2 = Grade("Grade 2")
    grade_3 = Grade("Grade 3")
    grade_1.add_course(chinese, math, science, chemistry)
    grade_1.del_course(math)
    grade_2.add_course(english, geography, chinese)
    grade_3.add_course(physics, math, science, chemistry)

    def __init__(self):
        while True:  # 进入系统 #
            print("----------School Manage IT--------------")
            print("Select you identity")
            print("Student press 1")
            print("Teacher press 2")
            print("Manager press 3")
            print("Exit press 4")
            print("----------------------------------------")
            selection = input("Enter your choice: ")
            if selection == "1":
                self._student_manage()

            elif selection == "2":
                self._teacher_manage()

            elif selection == "3":
                self._manager_manage()

            elif selection == "4":
                print("Thanks for you use!")
                break
            else:
                print("Invalid choice")

    def _student_manage(self):
        name = input("First give me your name: ")
        age = input("Next give me your age: ")
        sex = input("Last give me your sex: ")

        all_student_list = []
        for i in self.new_area.teacher_list:
            for j in i.grade_list:
                for k in j.student_list:
                    all_student_list.append(k.name)

        for i in self.old_area.teacher_list:
            for j in i.grade_list:
                for k in j.student_list:
                    all_student_list.append(k.name)
        all_student_list = list(set(all_student_list))

        if name not in all_student_list:
            new_student = Student(name, age, sex)  # 创建新学生 #
            print("----------------------------------------")
            print("Select your position")
            print("New area press 1")
            print("Old area press 2")
            position = input("Enter your position: ")
            if position == "1":
                new_student.area = self.new_area
            else:
                new_student.area = self.old_area

            all_grade_list = []
            for i in new_student.area.teacher_list:  # 展示所在校区的班级 #
                for j in i.grade_list:
                    print("----------------------------------------")
                    all_grade_list.append(j)
                    print(j.name)
                    for k in j.course_list:
                        print(k.name)
            all_grade_list = list(set(all_grade_list))

            length = len(all_grade_list)  # 学生选班级 #
            print("----------------------------------------")

            if length != 0:
                while True:
                    choice = input("Select your grade: ")
                    if length >= int(choice):
                        new_student.grade = all_grade_list[int(choice) - 1]
                        all_grade_list[int(choice) - 1].student_list.append(new_student)
                        print(f"The grade cost {all_grade_list[int(choice) - 1].total_price}$")
                        break
                    else:
                        print("Grade Added Error")
                print(f"Bye {new_student.name} Thanks you!")
            else:
                print("NO Grade Now")

        else:
            print("Duplicate Registration")

    def _teacher_manage(self):
        name = input("Please give me your name: ")

        all_teacher_list = []
        for i in self.new_area.teacher_list:
            all_teacher_list.append(i.name)
        for i in self.old_area.teacher_list:
            all_teacher_list.append(i.name)
        all_teacher_list = list(set(all_teacher_list))

        if name not in all_teacher_list:
            new_teacher = Teacher(name)  # 创建新老师 #
            print("----------------------------------------")
            print("Select your position")
            print("New area press 1")
            print("Old area press 2")
            position = input("Enter your position: ")
            if position == "1":
                new_teacher.area = self.new_area
                self.new_area.add_teacher(new_teacher)
            else:
                new_teacher.area = self.old_area
                self.old_area.add_teacher(new_teacher)

            all_grade = [self.grade_1, self.grade_2, self.grade_3]  # 展示所有班级 #
            for i in all_grade:
                print("----------------------------------------")
                print(i.name)
                for j in i.course_list:
                    print(j.name)

            print("----------------------------------------")  # 老师选班级 #
            print("Press 4 to exit")
            while True:
                choice = input("Select your grade: ")
                if choice == "1" and self.grade_1 not in new_teacher.grade_list:
                    new_teacher.add_grade(self.grade_1)
                elif choice == "2" and self.grade_2 not in new_teacher.grade_list:
                    new_teacher.add_grade(self.grade_2)
                elif choice == "3" and self.grade_3 not in new_teacher.grade_list:
                    new_teacher.add_grade(self.grade_3)
                elif choice == "4":
                    print(f"Bye {new_teacher.name} Thanks you!")
                    break
                else:
                    print("Grade Added Error")

        else:
            print("Duplicate Registration")

    def _manager_manage(self):
        while True:
            print("----------------------------------------")
            print("Select your position")
            print("All student press 1")
            print("All teacher press 2")
            print("All money press 3")
            print("Exit press 4")
            print("----------------------------------------")
            position = input("Enter your position: ")
            if position == "1":
                all_students_list = []
                for i in self.new_area.teacher_list:
                    for j in i.grade_list:
                        for k in j.student_list:
                            all_students_list.append(k)

                for i in self.old_area.teacher_list:
                    for j in i.grade_list:
                        for k in j.student_list:
                            all_students_list.append(k)
                all_students_list = list(set(all_students_list))
                print("All Students")
                for i in all_students_list:
                    print(i)

            elif position == "2":
                all_teachers_list = []
                for i in self.new_area.teacher_list:
                    all_teachers_list.append(i)
                for i in self.old_area.teacher_list:
                    all_teachers_list.append(i)
                print("All Teachers")
                for i in all_teachers_list:
                    print(i)

            elif position == "3":
                print("----------------------------------------")
                print("Select your position")
                print("New area press 1")
                print("Old area press 2")
                position = input("Enter your position: ")
                if position == "1":
                    money = 0
                    all_students_list = []
                    for i in self.new_area.teacher_list:
                        for j in i.grade_list:
                            for k in j.student_list:
                                all_students_list.append(k)
                    for i in all_students_list:
                        money += i.grade.total_price
                    print(f"All money in new area is {money}$")

                else:
                    money = 0
                    all_students_list = []
                    for i in self.old_area.teacher_list:
                        for j in i.grade_list:
                            for k in j.student_list:
                                all_students_list.append(k)
                    for i in all_students_list:
                        money += i.grade.total_price
                    print(f"All money in old area is {money}$")

            elif position == "4":
                print(f"Bye Manager Thanks you!")
                break

            else:
                print("Invalid choice")
