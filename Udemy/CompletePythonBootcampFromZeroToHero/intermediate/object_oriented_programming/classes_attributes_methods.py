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
Circle.pi = 314.159
print(circle.get_area())


class Square():
    def __init__(self, length:int) -> None:
        self.length = length
    def get_area(self):
        return self.length**2

from dataclasses import dataclass, field
@dataclass
class Square2():
    length: int = field(init=False, default=10) #init=false - class attribute (static variable)
    my_list: list[int] = field(default_factory=list)

    # def __init__(self, length:int, my_list: list[int] = []) -> None:
    #     my_list.append(10)
    #     self.length = length
    #     self.my_list= my_list
    #     pass

    def get_area(self):
        return self.length**2

my_list = [1]
s = Square2()
s2 = Square2()
s3 = Square2()



print(s.get_area(), s2.get_area(), s3.get_area())
Square2.length = 100
print(s.get_area(), s2.get_area(), s3.get_area())
print(str(s))
# Square2.length = 11
# print(s.get_area())