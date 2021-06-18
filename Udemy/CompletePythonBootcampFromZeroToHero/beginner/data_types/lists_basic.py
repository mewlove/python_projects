# Integers: int         3 300 200
# Floating point:       float  2.3  4.6  100.
# Strings: str          'Sam' "Sam" "2.0" "1000"
# List: list            [10, 'hello', 200.3]
# Dictionaries: dict    {"mykey":"value" , 'mykey2':'value2'}
# Tuples: tuple         (10,"hello",200.3)                      (immutable seq of objects) 
# Sets: set             {"a","b",1}                             (unordered unique collection)
# Booleans: bool        True, False
# (control + '/' for comments)

#Lists
my_list = [0,1,2,3,4,5]
print("\n")
print(f"my_list: {my_list}")
print(f"len(my_list): {len(my_list)}")
print(f"my_list[1]: {my_list[1]}")
print(f"my_list[1:]: {my_list[1:]}")
print(f"my_list[2:4]: {my_list[2:4]}")
print(f"my_list[::2]: {my_list[::2]}")
my_list[0] = 6
print("my_list[0] = 6")
print(f"my_list(new): {my_list}")
my_list.append(12)
print(f"my_list.append(12): {my_list}")
my_list.remove(2)
print(f"my_list.remove(2): {my_list}")

unsorted_list = ["r","f","a","w","c"]
print(f"unsorted_list: {unsorted_list}")
sorted_list = unsorted_list
sorted_list.sort()
print(f"sorted_list: {sorted_list}")
