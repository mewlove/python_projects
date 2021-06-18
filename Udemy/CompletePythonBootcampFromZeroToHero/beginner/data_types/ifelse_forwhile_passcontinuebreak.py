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

