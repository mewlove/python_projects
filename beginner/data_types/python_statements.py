# (control + '/' for comments)

#########################################################
#if elif else
# if some_condition:
#   #do something
# elif some_other_condition:
#   #do something different
# else:
#   #do something else
#########################################################
hungry = True

if hungry:
    print("I'm hungry!")
else:
    print("I'm not hungry'!")

zoo = 'Zoo'
library = 'Library'
bank = 'Bank'
from random import randint
rand = randint(0,3)

location = zoo
if rand == 0:
    location = zoo
elif rand == 1:
    location = library
else:
    location = bank

if location == 'Library':
    print("I'm at the Library")
elif location == 'Bank':
    print("I'm at the Bank!")
else:
    print(f"I am at the {location}")


#########################################################
#for loops
#########################################################
print("\n")
my_iterable  =  [1,2,3,4,5,6,7,8,9,10]
for index,item_name in enumerate(my_iterable):
    print(index,item_name)
list_sum = 0
for num in my_iterable:
    list_sum = list_sum + num
print(f"List Sum: {list_sum}")

mystring = "Hello World"
for char in mystring:
    print(char)

my_list_of_tuples = [(1,2),(3,4),(5,6),(7,8)]
for item in my_list_of_tuples:
    print(item)
print("\n")
for (a,b) in my_list_of_tuples:
    print(f"({b}, {a})")

d = {'k1':1,'k2':2,'k3':3}
for key,value in d.items():
    print(key,value)


#########################################################
#while loops
#########################################################
print("\n")
print("while loops")
increment = 0

while increment<5:
    print(f"Current increment: {increment}")
    increment += 1
else:
    print("Out Of While Loop")


#########################################################
#keywords pass, continue, break
#########################################################
x = [1,2,3]
for item in x:
    pass #does nothing

mystring = 'Sammy'
for c in mystring:
    if c == 'a':
        continue
    else:
        print(c)

x = 0
while True:
    if x > 5:
        break
    print(x)
    x += 1
print(x)

#########################################################
#Useful Operators in Python
#########################################################
print("Useful Operators in Python")
print("\n")
print("Range Function")
for num in range(0,10,2):
    print(num)

print("\n")
print("Enumerate Function")
word = 'abcde'
for items in enumerate(word):
    print(items)

print("\n")
print("Zip Function")
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
for item in zip(mylist1, mylist2):
    print(item)

print("\n")
print("In Function")
in_list = 'x' in ['x','y','z']
print(in_list)
in_list = '1' in ['x','y','z']
print(in_list)
in_list = 'r' in 'broom'
print(in_list)

print("\n")
print("Min Max Function")
mylist = [10,20,30,40,1000]
print(min(mylist))
print(max(mylist))

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist)
print(mylist)
from random import randint
print(randint(0,100))

######################################
## UNCOMMENT THIS SECTION FOR INPUT
# r = input("Enter a number: ")
# print(f"Number: {r}  has been entered.")
# no = float(r)
# print(f"Number: {r}  has been entered.")
#######################################


#########################################################
#List comprehensions!
#Some ways of creating Lists
#########################################################
print("\n")
print("List Comprehensions")

mylist = [letter for letter in 'Hello']
print(mylist)

mylist = [x**2 for x in range(0,11)]
print(mylist)

mylist = [x**2 for x in range(0,11) if (x+1) % 2 == 0]
print(mylist)

mylist = [x**2 if (x+1) % 2 == 0 else x**3 for x in range(0,11) ]
print(mylist)

mylist = [x*y for x in [2,4,6] for y in [1, 10, 100] ]
print(mylist)

names = ['nameA','nameB','nameC']
values = [2,4,6]
my_dict = {name: value for name, value in zip(names, values)}
print(my_dict)


#########################################################