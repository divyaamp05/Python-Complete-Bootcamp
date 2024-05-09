class A:                         ### Using Method Resolution Order(MRO) we can call both init and methods
    def __init__(self):
        print("Init in A")
    def feature1(self):
        print("Feature 1-A is working")
    def feature2(self):
        print("Feature 2 is working")

class B:
    def __init__(self):
        print("Init in B")
    def feature1(self):
        print("Feature 1-B is working")
    def feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("Init in C")
    def feature4(self):
        super().feature4()
        print("Feature 4 is working")

c=C()
c.feature1()
c.feature4()
