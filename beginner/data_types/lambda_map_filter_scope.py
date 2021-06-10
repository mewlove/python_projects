# (control + '/' for comments)


#map function
def square(num:int):
    return num**2

my_nums = [1,2,3,4,5]
my_nums_squared = list(map(square, my_nums))
print(my_nums_squared)

#filter function
def check_even(num:int):
    return num%2 == 0
my_nums = [1,2,3,4,5,6]
my_nums_even = list(filter(check_even, my_nums))
print(my_nums_even)

#lambda expression
my_nums_squared = list(map(lambda num: num**2, my_nums))
print(my_nums_squared)

names = ["Sally","Eva","Dolly"]
reversed_names = list(map(lambda x: x[::-1].lower().capitalize(),names))
print(reversed_names)


###############################################
# Nested statements and scope
###############################################
x =25
def printer():
    x = 50 
    return x
printer()
print(x)
#prints 25

name = "GLOBAL"
def func():
    name = "ENCLOSING"
    def hello():
        name = "LOCAL"
        print(name)
    hello()
    print(name)

func()


x = 25
def func1(r:int):
    r = 50
    print(r)

func1(x)
print(x)

def func2(r:int):
    global x  #global variable
    x = 50
    print(x)

func2(x)
print(x)