# (control + '/' for comments)
mylist = [1,2,3,4,5]
help(mylist.insert)

#how to write functions
def name_of_function(a_parameter:str):
    '''
    multiline comments
    do something here
    '''
    print("Parameter: "+a_parameter)

def function_with_return(a:int, b:int):
    '''
    multiline comments
    '''
    return a+b

def function_with_default(d:str = "Default"):
    '''
    multiline comments
    '''
    print(d)

function_with_default()
#print(function_with_return('10','20'))  #this will give 1020 instead of 30

def check_even(number:int):
    return number % 2 == 0
print(f"Number: 10 is even? {check_even(10)}")
print(f"Number: 9 is even? {check_even(9)}")

def even_numbers_list(num_list:list[int]):
    even_numbers: list[int] = []

    for item in num_list:
        if item % 2 == 0:
            even_numbers.append(item)
        else:
            pass
    return even_numbers

print(even_numbers_list([1,2,3,4,5,6,7,8,9,10]))

work_hours = [('Abby',100),('Bob',400),('Cassie',800)]
def employee_of_the_month_check(work_hours:list[tuple[str,int]]):
    current_max:int = 0
    employee_of_the_month:str = ""

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass
    return (employee_of_the_month,current_max)

print(employee_of_the_month_check(work_hours))

list_to_be_shuffled = [1,2,3,4,5,6,7,8,9,10]
from random import shuffle
from typing import TypeVar
T = TypeVar('T')
def shuffle_list(list_to_shuffle:list[T]) -> list[T]:
    temp_shuffle_list:list[T] = list_to_shuffle
    shuffle(temp_shuffle_list)
    return temp_shuffle_list
print(shuffle_list(list_to_be_shuffled))

def guessed_correctly(ball_positions:list[str],guess:int):
    if 0<=guess<=2 and ball_positions[guess] == 'O':
        return True
    else:
        print("Wrong! ")
        return False

def play_game(ball_positions:list[str]):
    print(f"Current Ball Position: {ball_positions}")
    player_guess:int = int(input("Where is the ball now? 0, 1 or 2? "))
    temp_ball_positions:list[str] = shuffle_list(ball_positions)
    print(f"Current Ball Position: {temp_ball_positions}")
    while(not guessed_correctly(temp_ball_positions,player_guess)):
        player_guess = -1
        while player_guess < 0 or player_guess >2:
            player_guess = int(input("Where is the ball now? 0, 1 or 2? "))
        temp_ball_positions = shuffle_list(temp_ball_positions)
        print(f"Current Ball Position: {temp_ball_positions}")
    print("Correct!")

#play_game([' ','O',' '])


'''
*args and **kwargs
*args (with one asterisk) represents parameters in tuples
**kwargs (with two asterisks) represents parameters in dictionary
'''
def sum_all(*numbers:int): # should always use *args (this example is only to showcase possibilities)
    total_sum:int = 0
    for i in numbers:
        total_sum += i
    return total_sum

print(sum_all(1,2,3,4,5,6,7,8,9,10))

def myfunc (**kwargs:str):
    print(kwargs)
myfunc(fruit='apple',veggie='lettuce')

def myfunc2(*args:int, **kwargs:str):
    print(f"I would like {args[0]} {kwargs['food']}")

myfunc2(10,20,30,40,50,drink='water',food='eggs',soda='coke')

def all_even(*args:int):
    return [x for x in args if x%2 == 0]

print(all_even(1,2,3,4,5,6,7,8,9,10))

def old_macdonald(name:str):
    a = [item[1].upper() if (item[0]==0 or item[0]==3) else item[1] for item  in enumerate(name)]
    return "".join(a)
