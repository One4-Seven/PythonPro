class Teacher:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.grade_list = []

    def add_grade(self, grade):
        self.grade_list.append(grade)
        print("Grade Added")

    def del_grade(self, grade):
        if grade in self.grade_list:
            self.grade_list.remove(grade)
            print("Grade Removed")

    def __str__(self):
        length = len(self.grade_list)
        if length == 0:
            return f"Name: {self.name} Area: {self.area.position} Grades: None"
        elif length == 1:
            return f"Name: {self.name} Area: {self.area.position} Grades: {self.grade_list[0].name} {self.grade_list[0].total_price}$"
        elif length == 2:
            return f"Name: {self.name} Area: {self.area.position} Grades: {self.grade_list[0].name} {self.grade_list[0].total_price}$, {self.grade_list[1].name} {self.grade_list[1].total_price}$"
        else:
            return f"Name: {self.name} Area: {self.area.position} Grades: {self.grade_list[0].name} {self.grade_list[0].total_price}$, {self.grade_list[1].name} {self.grade_list[1].total_price}$, {self.grade_list[2].name} {self.grade_list[2].total_price}$ "
