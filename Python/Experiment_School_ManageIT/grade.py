class Grade:
    def __init__(self, grade_name):
        self.name = grade_name
        self.course_list = []
        self.student_list = []
        self.total_price = 0

    def add_course(self, *course):
        for i in course:
            self.course_list.append(i)
            self.total_price += i.price
        print("Course Added")

    def del_course(self, course):
        if course in self.course_list:
            self.course_list.remove(course)
            self.total_price -= course.price
            print("Course Removed")
        else:
            print("Course Not Found")

    def add_student(self, student):
        self.student_list.append(student)
        print("Student Added")

    def del_student(self, student):
        if student in self.student_list:
            self.student_list.remove(student)
            print("Student Removed")
        else:
            print("Student Not Found")
