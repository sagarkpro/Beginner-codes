class Student:
    def __init__(self, name, rollno, std, percentageobt):
        self.name = name
        self.rollno = rollno
        self.std = std
        self.percentageobt = percentageobt

    def printClassA(self):
        return f"My name is {self.name}, and my roll number is {self.rollno}. I study in {self.std}th and this is my last year's percentage : {self.percentageobt}"

    def __add__(self, other):
        return self.percentageobt + other.percentageobt

    def __gt__(self, other):
        if self.percentageobt > other.percentageobt :
            return f"{self.name} has scored higher than {other.name}"
        else :
            return f"{other.name} has scored higher than {self.name}"

student1 = Student("Sagar", 69, 3, 69)
student2 = Student("Bissal", 70, 3, 60)
print(student1 + student2)
print(student1 > student2)