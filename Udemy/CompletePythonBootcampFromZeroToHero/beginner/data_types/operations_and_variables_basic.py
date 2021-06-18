# Integers: int         3 300 200
# Floating point:       float  2.3  4.6  100.
# Strings: str          'Sam' "Sam" "2.0" "1000"
# List: list            [10, 'hello', 200.3]
# Dictionaries: dict    {"mykey":"value" , 'mykey2':'value2'}
# Tuples: tuple         (10,"hello",200.3)                      (immutable seq of objects) 
# Sets: set             {"a","b",1}                             (unordered unique collection)
# Booleans: bool        True, False
# (control + '/' for comments)

import math

# MATHEMATICS OPERATIONS
print("\n")
print("Mathematics Operations")
print("Addition: 7 + 4 =",7 + 4)
print("Subtract: 7 - 4 =",7 - 4)
print("Multiply: 7 * 4 =",7 * 4)
print("Division: 7 / 4 =",7 / 4)
print("Modulo: 7 % 4 =",7 % 4)
print("Power: 2 ** 3 =",2 ** 3)
print("Sqrtt 4: 4 ** 0.5 = ", 4 ** 0.5)
print("Sqrt 4: sqrt(4) = ", math.sqrt(4) )
print(" 1==1 ", (1 == 1) )
print(" 1>2 ", 1 > 2 )
print(" 1<2 ", 1 < 2 )
print(" 1<2<3 ", 1 < 2 < 3 )
print(" 1<2 and 2<3 ", 1 < 2 and 2 < 3 )
print(" 'h' != 'h' ", 'h' != 'h')
print(" 1<2 or 2>3 ", 1<2 or 2>3 )
print(" not 100>0 ", not 100>0 )

# ASSIGNING VARIABLES
print("\n")
print("Assigning Variables")
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print("type(my_income): ",type(my_income))
print("type(tax_rate): ",type(tax_rate))
print("type(my_taxes): ",type(my_taxes))
print("my_taxes: ",my_taxes)


