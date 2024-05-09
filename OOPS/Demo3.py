class Person:
    def __init__(self):
        self.name="Diya"
        self.age=19
    def update(self):
        self.age=20
    def compare(self,other):
        if(self.age==other.age):
            True
        else:
            False

p1=Person()
p2=Person()
p1.name="Siya"
p1.age=18

p1.update()

if p1.compare(p2):
    print("They are same")
else:
    print("They are different")

print(p1.name,p1.age)
print(p2.name,p2.age)
