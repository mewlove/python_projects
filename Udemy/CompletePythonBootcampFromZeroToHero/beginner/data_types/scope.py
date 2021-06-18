# (control + '/' for comments)

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