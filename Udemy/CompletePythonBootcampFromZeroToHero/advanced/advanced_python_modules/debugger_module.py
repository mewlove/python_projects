# (control + '/' for comments)

x = [1,2,3]
y = 2
z = 3

import pdb

result = y + z

pdb.set_trace() #See terminal - type variables and operations (such as x + z) to see what is wrong
result2 = x + z #type:ignore  #ERROR
