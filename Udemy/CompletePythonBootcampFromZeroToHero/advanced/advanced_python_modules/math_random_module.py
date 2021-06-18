# (control + '/' for comments)

import math

value = 4.35
print(f"floor: {math.floor(value)}")
print(f"ceiling: {math.ceil(value)}")
print(f"round: {round(value)}")
print(f"round(3.5): {round(3.5)}")
print(f"round(3.4): {round(3.4)}")
print(f"pi: {math.pi}")
print(f"e: {math.e}")
print(f"inf: {math.inf}")
print(f"nan: {math.nan}")

print(f"log e = {math.log(math.e)}")
print(f"log (100,10)) = {math.log(100,10)}")

#research on numpy for more math functions


import random
print()
print("!!!!!! random.randint(low,high) is inclusive of both low and high!!!!!!!!!")
print()
r = random.randint(0,2) #inclusive of 0 and 2
print(f"Random without seed: {r}")
r = random.randint(0,2) #inclusive of 0 and 2
print(f"Random without seed: {r}")
r = random.randint(0,2) #inclusive of 0 and 2
print(f"Random without seed: {r}")

random.seed(74)
r = random.randint(0,2) #inclusive of 0 and 2
print(f"Random with seed: {r}")
r = random.randint(0,2) #inclusive of 0 and 2
print(f"Random with seed: {r}")
r = random.randint(0,2) #inclusive of 0 and 2
print(f"Random with seed: {r}")

random.seed()
mylist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#sample choice
print(f"choose a number from {mylist}:\n{random.choice(mylist)}")


#sample choice with replacement 
print(f"Chooose 10 numbers (with replacement) from {mylist}:\n{random.choices(population=mylist,k=10)}")


#sample choice with replacement 
print(f"Chooose 10 numbers (without replacement) from {mylist}:\n{random.sample(population=mylist,k=10)}")


r = random.uniform(0,1) #inclusive of 0 nd 1
print(f"random.uniform (0.0,1.0 - inclusive) : {r}")


r = random.random() #inclusive of 0 nd 1
print(f"random.random (0.0,1.0 - exclusive) : {r}")