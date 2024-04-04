class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)
            return True
        else:
            print("No space available in the class for more students.")
            return False

    def get_average_grade(self):
        if self.grades:
            return "{:.2f}".format(sum(self.grades) / len(self.grades))
        else:
            return "N/A"

    def __repr__(self):
        students_str = ", ".join(self.students)
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {students_str}. Average grade: {average_grade}"


class1 = Class("Class 1")
class1.add_student("Alice", 95)
class1.add_student("Bob", 88)
class1.add_student("Charlie", 72)
print(class1)

class2 = Class("Class 2")
class2.add_student("David", 90)
class2.add_student("Emma", 85)
class2.add_student("Frank", 78)
print(class2)
