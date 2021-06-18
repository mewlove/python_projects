# (control + '/' for comments)

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