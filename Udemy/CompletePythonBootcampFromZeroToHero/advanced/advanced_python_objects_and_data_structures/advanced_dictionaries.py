# (control + '/' for comments)


d = {'k1':1,'k2':2}
print(d)
d_compre = {x:x**2 for x in range(10)}
print(d_compre)
d_compre = {k:v**2 for k,v in zip(['a','b','c'],range(3))}
print(d_compre)