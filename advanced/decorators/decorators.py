# (control + '/' for comments)
from typing import Callable


def return_func(func:str=""):
    def greet():
        return "hello!"
    def welcome():
        return "welcome!"
    
    if func == "greet":
        return greet
    elif func == "welcome":
        return welcome
    else:
        return welcome


func1 = return_func("greet")

def take_func(func:Callable[[], str]):
    print(func())

take_func(func1)



def new_decorator(original_func): # type: ignore
    def wrap_func():
        print("Some extra code, before original function")
        original_func()
        print("Some extra code, after original function")
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()