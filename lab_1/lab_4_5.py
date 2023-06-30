class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display(self):
        print("First name: {}".format(self.firstname))
        print("Last name: {}".format(self.lastname))
        print("Age: {}".format(self.age))

class Student(Person):
    student_count = 0

    def __init__(self, firstname, lastname, age, recordBook):
        super().__init__(firstname, lastname, age)
        Student.student_count += 1
        self.studentID = Student.student_count
        self.recordBook = recordBook

    def display(self):
        super().display()
        print("Student ID: {}".format(self.studentID))
        print("Record book: {}".format(self.recordBook))

class Professor(Person):
    professor_count = 0

    def __init__(self, firstname, lastname, age, degree):
        super().__init__(firstname, lastname, age)
        Professor.professor_count += 1
        self.professorID = Professor.professor_count
        self.degree = degree

    def display(self):
        super().display()
        print("Professor ID: {}".format(self.professorID))
        print("Degree: {}".format(self.degree))


student1 = Student("John", "Doe", 20, [5, 4, 4, 3])
student2 = Student("Jane", "Doe", 19, [5, 5, 4, 4])
student3 = Student("Bob", "Smith", 21, [3, 3, 2, 2])

student1.display()
student2.display()
student3.display()

professor1 = Professor("Alice", "Johnson", 40, "PhD")
professor2 = Professor("Bob", "Johnson", 45, "PhD")
professor3 = Professor("Charlie", "Brown", 50, "PhD")

professor1.display()
professor2.display()
professor3.display()
