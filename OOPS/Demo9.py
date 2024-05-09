class A:                                 ### Multiple Inheritance
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B:
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def feature5(self):
        print("Feature 5 is working")
a=A()
a.feature1()
a.feature2()
b=B()
b.feature3()
b.feature4()
c=C()
c.feature1()
c.feature3()
c.feature5()
