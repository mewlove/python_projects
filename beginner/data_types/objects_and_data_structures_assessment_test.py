# Objects and Data Structures Assessment Test
## Test your knowledge
# Write (or just say out loud to yourself) a brief description of all the following Object Types 
# and Data Structures we've learned about. 
# Really this is just to test if you know the difference between these, 
# so feel free to just think about it, since your answers are self-graded.

# Numbers: integers for whole numbers or floating point for numbers with decimal point representations for example 2 or 2.0
# Strings: a sequence of characters placed within a double or single quotation mark, for example 'test' or "test"
# Lists: the container for a sequence of objects e.g [1,"hello",3.0]
# Tuples: a immutable list
# Dictionaries: a container that consists of a sequence of key,value pairs e.g {"key1":"value1", "key2":"value2"}

import math

## Numbers
# Q1 Write an equation that uses multiplication, division, an exponent, addition, and subtraction 
# # that is equal to 100.25.
q1 = (10 + 200 * 2 - 9) / 4
print(q1)

# Q2a What is the value of the expression 4 * (6 + 5)
q2a = 44
print(q2a == 4 * (6 + 5))
#Q2b What is the value of the expression 4 * 6 + 5
q2b = 29
print(q2b == 4 * 6 + 5)
#Q2c What is the value of the expression 4 + 6 * 5
q2c = 34
print(q2c == 4 + 6 * 5)

#q3 What is the *type* of the result of the expression 3 + 1.5 + 4?
q3 = float
print(q3 == type(3 + 1.5 + 4))

#q4a/b What would you use to find a number’s square root, as well as its square?
q4a = 2 ** 2
q4b = math.sqrt(4)
print(q4a)
print(q4b)

#q5 Given the string 'hello' give an index command that returns 'e'.
q5 = 'hello'[1]
print(q5)

#q6 Reverse the string 'hello' using slicing:
s ='hello'
q6 = s[::-1]
print(q6)

#q7a/b Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'
q7a = s[4]
q7b = s[-1]
print(q7a)
print(q7b)

#q8a/b Build this list [0,0,0] two separate ways.
q8a = [0,0,0]
q8b = [0]*3
print(q8a)
print(q8b)

########## Commented due to bad typing
# #q9 Reassign 'hello' in this nested list to say 'goodbye' instead:
# list3 = [1,2,[3,4,'hello']]
# q9 = list3
# q9[2][2] = 'goodbye'
# print(q9)

#q10 Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
q10 = list4
print(q10)


## Dictionaries
#q11a/b/c/d Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
q11a = d['simple_key']
print(q11a)

d = {'k1':{'k2':'hello'}}
q11b = d['k1']['k2']
print(q11b)

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
q11c = d['k1'][0]["nest_key"][1][0]
print(q11c)

################# Commented due to bad typing
# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# q11d = d['k1'][2]['k2'][1]['tough'][2][0]
# print(q11d)


## Tuples
#q12 What is the major difference between tuples and lists?
# Tuples are immutable but lists are not

#q13 How do you create a tuple?
q13 = ('here','is','a','tuple')
print(q13)

## Sets 
# q14 What is unique about a set?
# sets contain only unique objects

#q15 Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
q16 = set(list5)
print(q16)

### Booleans
# For the following quiz questions, we will get a preview of comparison operators. 
# In the description below, a=3 and b=4.
# ==  If the values of two operands are equal, then the condition becomes true.  e.g (a == b) is not true.
# != If values of two operands are not equal, then condition becomes true. e.g (a != b) is true.
# > If the value of left operand is greater than the value of right operand, then condition becomes true. e.g (a > b) is not true.
# < If the value of left operand is less than the value of right operand, then condition becomes true. e.g (a < b) is true.
# >= If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. e.g (a >= b) is not true.
# <= If the value of left operand is less than or equal the value of right operand, then condition becomes true. e.g (a <= b) is true.

# q15a/b/c/d/e What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)
# 2 > 3
# 3 <= 2
# 3 == 2.0
# 3.0 == 3
# 4**0.5 != 2
a15a = False
a15b = False
a15c = False
a15d = True
a15e = False
print(a15a == (2>3))
print(a15b == (3 <= 2))
print(a15c == (3 == 2.0))
print(a15d == (3.0 == 3))
print(a15e == (4**0.5 != 2))

##### Question 16 commented as it uses bad typing
# #q16 Final Question: What is the boolean output of the cell block below?
# # two nested lists
# l_one = [1,2,[3,4]]
# l_two = [1,2,{'k1':4}]

# # True or False?
# #l_one[2][0] >= l_two[2]['k1']
# test_q16 = l_one[2][0] >= l_two[2]['k1']
# q16 = False
# print(q16 == test_q16)

#END TEST

