#Assignment 1
#Class
#Part 1 - creating a class, adding attributes and methods, and using constructors
class Rock:
    def __init__(self,name,color,hardness):
        self.name = name #instance variable for a name
        self.color = color #instance variable for a color
        self.hardness = hardness #instance variable for a hardness
#define a method to display the rock details
    def display_details(self):
        print(f"Rock Name: {self.name}, Color: {self.color}, Hardness: {self.hardness}")
#create an object of the class
granite = Rock("Granite", "Gray", 6) #creating an object of the class
granite.display_details() #calling the display_details method


#Qn2 Demonstrate the use of inheritance
class PreciousRock(Rock):
    def __init__(self, name, color, hardness,value):
       self.name = name
       self.color = color
       self.hardness = hardness
       self.value = value
    def display_details(self):
        print(f"Rock Name: {self.name}, Color: {self.color}, Hardness: {self.hardness}, Value: {self.value}")
#creating an object of the class
diamond = PreciousRock("Diamond", "Colorless", 10, 10000) #creating an object of the class
diamond.display_details() #calling the display_details method