class Car:
    wheels=4                    ## Static (or) class varibales
    def __init__(self):         ## Default Constructor
        self.name="BMW"
        self.mil=10

c1=Car()
c2=Car()
c2.name="Benz"
c2.mil=30

print(c1.name,c1.mil,c1.wheels)
print(c2.name,c2.mil,c2.wheels)
