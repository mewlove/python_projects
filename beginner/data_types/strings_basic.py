# Integers: int         3 300 200
# Floating point:       float  2.3  4.6  100.
# Strings: str          'Sam' "Sam" "2.0" "1000"
# List: list            [10, 'hello', 200.3]
# Dictionaries: dict    {"mykey":"value" , 'mykey2':'value2'}
# Tuples: tuple         (10,"hello",200.3)                      (immutable seq of objects) 
# Sets: set             {"a","b",1}                             (unordered unique collection)
# Booleans: bool        True, False
# (control + '/' for comments)

# STRING DATATYPE
print("\n")
print("Strings!")
hello_str = "Hello"
print("hello_str: ",hello_str)
print("len(hello_str): ",len(hello_str))
print("hello_str[0]: ",hello_str[0])
print("hello_str[1]: ",hello_str[1])
print("hello_str[-1]: ",hello_str[-1])
print("hello_str[-2]: ",hello_str[-2])

print("\n")
print("String slicing!")
alphabet_str = "abcdefghijklmnopqrstuvwxyz"
print("alphabet_str: ",alphabet_str)
print("alphabet_str[2]: ",alphabet_str[2])
print("alphabet_str[2:]: ",alphabet_str[2:])
print("alphabet_str[2:6]: ",alphabet_str[2:6])
print("alphabet_str[:3]: ",alphabet_str[:3])
print("alphabet_str[:-1]: ",alphabet_str[:-1])
print("String stepsize:")
print("alphabet_str[::2]: ",alphabet_str[::2])
print("alphabet_str[::2]: ",alphabet_str[::-1])

print("\n")
print("String Concatenation!")
string_front = "Hello"
string_middle = " "
string_back = "World"
print("string_front: '{}',   string_middle: '{}',   string_back: '{}' ".format(string_front,string_middle,string_back))
print("string_front+string_middle+string_back: ",string_front+string_middle+string_back)
letter_z = "z"
print("letter_z: ",letter_z)
print("letter_z * 10: ",letter_z*10)
hello_world = "Hello World"
print("hello_world: ",hello_world)
print("hello_world.split(): ",hello_world.split())
print("hello_world.split('o'): ",hello_world.split('o'))


print("\n")
print("String Interpolation!")
print('The {} {} {}'.format("fox","brown","quick"))
print('The {2} {1} {0}'.format("fox","brown","quick"))
print('The {q} {b} {f}'.format(f="fox",b="brown",q="quick"))
float_value = 10.123456789
print("float_value: ",float_value)
print("The float value is {fv:.3f} (3dp)".format(fv = float_value))
print("The float value is {fv:15.3f} (15 width)".format(fv = float_value))
large_float_value = 10000000000.123456789
print("The large float value is {lfv:,} (Note the commas)".format(lfv = large_float_value))
print("\n")
print("Using f' (f' string require Python 3.6)")
print(f"Using f' to format {large_float_value:,}.")
name_jose = "Jose"
print("name_Jose: ",name_jose)
print(f"His name is {name_jose}.")
