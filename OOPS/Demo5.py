class Student:
    school="BVRIT"                     ### Class or Static Variable

    def __init__(self,m1,m2,m3):       ### Instance variables
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):                     ### Instance Method
         print((self.m1+self.m2+self.m3)/3)
    @classmethod                       ### Class method
    def get_school(cls):
        print(cls.school)

    @staticmethod                      ### Static Method
    def info():
        print("Welcome to BVRIT")

s1=Student(89,34,56)
s2=Student(56,27,98)

s1.avg()
s2.avg()
Student.get_school()
Student.info()