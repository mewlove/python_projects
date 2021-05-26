# Integers: int         3 300 200
# Floating point:       float  2.3  4.6  100.
# Strings: str          'Sam' "Sam" "2.0" "1000"
# List: list            [10, 'hello', 200.3]
# Dictionaries: dict    {"mykey":"value" , 'mykey2':'value2'}
# Tuples: tuple         (10,"hello",200.3)                      (immutable seq of objects) 
# Sets: set             {"a","b",1}                             (unordered unique collection)
# Booleans: bool        True, False
# (control + '/' for comments)

from typing import TypedDict


# DICTIONARY BASICS
my_dict = {'key1':'value1', 'key2':'value2'}
print("\n")
print(f"my_dict: {my_dict}")
print(f"my_dict['key2']: {my_dict['key2']}")
print(f"my_dict.get('key3'): {my_dict.get('key3')}")
d = {'k1':100,'k2':200,'k3':300}
print(f"d: {d}")
print(f"d.keys(): {d.keys()}")
print(f"d.values(): {d.values()}")
print(f"d.items(): {d.items()}")

nested_dict_type = TypedDict('nested_dict_type', {
    'list': list[str],
    'dict': dict[str, str],
})

nested_dict: nested_dict_type = {'list':['a','b','c'], 'dict':{'k1':'v1','k2':'v2'}}
print(f"nested_dict: {nested_dict}")
print(f"nested_dict['list']: {nested_dict['list']}")
print(f"nested_dict['list'][0]: { nested_dict['list'][0] }")
print(f"nested_dict['dict']: {nested_dict['dict']}")

print(f"nested_dict['dict']['k1']: {nested_dict['dict']['k1']}")
nested_dict = {'list':['a','b','c'], 'dict':{'k1':'v1','k2':'v2'}}



# TUPLE BASICS
# tuples are immutable (items in tuples, once set, cannot be changed)
my_tuple_1 = (2,2,3,3,4,4)
my_list:list[int] = [2,2,3,3,4,4]
print("\n")
print(f"my_tuple_1: {my_tuple_1}   type(my_tuple_1): {type(my_tuple_1)}")
print(f"my_list: {my_list}   type(my_list): {type(my_list)}")
print(f"my_tuple_1[1]: {my_tuple_1[1]}")
print(f"my_tuple_1[1:4]: {my_tuple_1[1:4]}")
print(f"my_tuple_1.count(3): {my_tuple_1.count(3)}")

my_list_2 = [{ 'id': 1}, { 'id': 2},{ 'id': 3},{ 'id': 3}, { 'id': 4}]
print(my_list_2)
my_list_2.remove({ 'id': 3})
print(my_list_2)

enumerate_list = enumerate(my_list)
# [(0, 2), (1, 2), (2, 3), (3, 3) ..]
filtered_list = (index for index, value in enumerate_list if value == 5)
# (2, 3)
index_3 = next(filtered_list, -1)
# 2
if index_3 != -1:
    # index_3 = 2
    my_list.pop(index_3)

print(f"my_list index 3: {index_3}")
print(f"my_list after remove index 3: {my_list}")

# SETS BASICS
# Set is a collection of UNIQUE values
myset:set[int] = set()
myset.add(1)
print("\n")
print(f"myset: {myset}")
my_list = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
print(f"my_list: {my_list}")
print(f"set(my_list): {set(my_list)} gives unique values")
print(f"set('Mississippi'): {set('Mississippi')}")
