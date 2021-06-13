# (control + '/' for comments)

class Dog():
    # CLASS OBJECT ATTRIBUTE
    # Same for all instances of the class
    animal_classification = "mammal"

    def __init__(self, breed:str="", name:str="") -> None:
        self.breed = breed
        self.name = name
    
    #Operations/Actions --> Methods
    def bark(self):
        print(f"WOOF! My name is {self.name}")

dog = Dog("Lab","Frankie")
dog.bark()

class Circle():
    pi = 3.14159

    def __init__(self, radius:int = 1) -> None:
        self.radius = radius
    
    def get_circumference(self):
        return 2* Circle.pi * self.radius
    
    def get_area(self): 
        return Circle.pi * self.radius * self.radius

circle = Circle()
print(circle.get_circumference())
print(circle.get_area())