class Student:
    major="CSE"
    def __init__(self,rollNum,name):
        self.rollNum=rollNum
        self.name=name
s1 = Student(1,"Neeraj")
print(s1.major)
print(s1.rollNum)
print(s1.name)
print(Student.major)