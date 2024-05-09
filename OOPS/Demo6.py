class Student:                                 ### Inner class
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno = rollno
        self.marks=marks


    def show(self):
        print("Name:",self.name,"Rollno:",self.rollno,"Marks:",self.marks)

    class Laptop:
        def __init__(self):
            self.brand="DELL"
            self.cpu="i7"
        def show(self):
            print("Brand:",self.brand,"CPU:",self.cpu)



s1=Student("Palak","23","90")
s2=Student("Payal","26","98")
s1.show()
s2.show()
lap1=Student.Laptop()
lap1.show()
lap2=Student.Laptop()
lap2.show()