class Student:
    def __int__(self, name):
        self.name = name
        self._grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self._grade = grade
        else:
            raise ValueError("Grade must be between 0 and 100")

    def get_grade(self):
        return self._grade

    def get_status(self):
        if self._grade >= 60:
            return "Passed"
        else:
            return "Failed"

student = Student()
student.set_grade(50)
print(student.get_grade())
print(student.get_status())
