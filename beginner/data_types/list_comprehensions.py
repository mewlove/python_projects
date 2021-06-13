# (control + '/' for comments)


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