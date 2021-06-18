# (control + '/' for comments)

'''
Inheritance
'''
class Animal():
    def __init__(self) -> None:
        print("Animal Created")
    def who_am_i(self)-> None:
        print("I am an animal")
    def eat(self)-> None:
        print("I am eating")
    def speak(self)->None:
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()
        print("Dog Created")
    def who_am_i(self) -> None:
        print("I am a dog")

dog = Dog()
dog.who_am_i()
dog.eat()



'''
Polymorphism (Same method different class)
'''
class Cat(Animal):
    def __init__(self) -> None:
        pass
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def __init__(self) -> None:
        pass
    def speak(self):
        print("Squeak!")
cat = Cat()
mouse = Mouse()

pets  = [cat,mouse]
for pet in pets:
    pet.speak()

