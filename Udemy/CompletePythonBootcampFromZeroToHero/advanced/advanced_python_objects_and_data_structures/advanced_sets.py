# (control + '/' for comments)


s = {1,2,3}
s_copy = s.copy()
s.add(4)
print(s)
print(s_copy)

print(f"difference: {s.difference(s_copy)}")

s = {1,2,3}
s_2 = {1,4,5}
s.difference_update(s_2) #only keep all elements that are in s that is different from the set s_2
print(f"difference_update-  s: {s}   s_2: {s_2}")  


s = {1,2,3}
s_2 = {1,4,5}
s_2.difference_update(s) #only keep all elements that are in s_2 that is different from the set s
print(f"difference_update-  s: {s}   s_2: {s_2}") 


s = {1,2,3,4,5,6,7,8,9,10}
s.discard(4)
print(f"discard 4 from s: {s}")

s = {1,2,4}
s_2 = {1,3,4}
print(f"intersection: {s.intersection(s_2)}")

s.intersection_update(s_2) #only keep all intersecting elements between s and s_2
print(f"intersection_update-  s: {s}   s_2: {s_2}") 


s = {1,2,3,5,6,7}
s_2 = {4,10}
print(f"isdisjoint: {s.isdisjoint(s_2)}")


s = {1,2}
s_2 = {1,2,6}
print(f"issubset: {s.issubset(s_2)}")
print(f"issuperset: {s_2.issuperset(s)}")


s = {1,2,5}
s_2 = {2,3,4}
print(f"union: {s.union(s_2)}")
print(f"difference: {s.difference(s_2)}")
print(f"symmetric_difference: {s.symmetric_difference(s_2)}")