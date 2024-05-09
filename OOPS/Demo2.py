class person:
    def __init__(self):               # Default Constructor
        print("Eyes: To see")
        print("Ears: To hear")
        print("Nose: To smell")
        print("Mouth: To taste")
        print("Skin: To touch")
    def eat(self):                #Instance Method
        print("Eat:4 times a day")
    def sleep(self):              #Instance Method
        print("Sleep:8 hours per day")
p1=person()
p1.eat()
p1.sleep()