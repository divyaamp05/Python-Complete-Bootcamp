class A:                                            ### Super Method()
    def __init__(self):
        print("Init in A")
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B(A):
    def __init__(self):
        super().__init__()
        print("Init in B")
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

b=B()

## We created a obj in class B.Since there is a constructor in class B init in B is called.
## But here we call super method which is used to call all the inits in parent class

