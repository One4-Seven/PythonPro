class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.area = None
        self.grade = None

    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Sex: {self.sex} Area: {self.area.position} Grade: {self.grade.name}"
