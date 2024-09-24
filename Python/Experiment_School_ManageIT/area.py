class Area:
    def __init__(self, position):
        self.position = position
        self.teacher_list = []

    def add_teacher(self, teacher):
        self.teacher_list.append(teacher)
        print("Teacher Added")

    def del_teacher(self, teacher):
        self.teacher_list.remove(teacher)
        print("Teacher Removed")



