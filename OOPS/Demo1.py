class Computer:
    def __init__(self,cpu,ram):   #Parameterized Constructor
        self.cpu = cpu
        self.ram = ram
    def config(self):             # Instance method
        print("CPU:",self.cpu,"RAM:",self.ram)

c1=Computer("i5","8gb")           #Object creation
c2=Computer("i6","16gb")
c1.config()
c2.config()


