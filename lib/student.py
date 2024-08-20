from user import User

class Student(User):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)  # Pass both name and age to the User constructor
        print(f"Student {self.name} is in the class room")
        self.student_id = student_id
        self.grade = grade

    def login(self):
        print(f"Student {self.name} is in the class")
        self.in_class = True

my_name = Student("Amir", 20, 8996, 320)
