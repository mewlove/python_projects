a = 0
b = 0

try:
    a = int(input("numerator: "))
except ValueError:
    print("a is not an int, a set to 0")
except:
    print("No idea what kind of error this is")

try:
    b = int(input("divisor: "))
except ValueError:
    print("b is not an int, b set to 0")
except:
    print("No idea what kind of error this is")

c=1

try:
    c = a/b
# except ZeroDivisionError:
#     print(f"code error at: {a}/{b} -- ZeroDivisionError: division by zero")
except TypeError:
    print(f"code error at: {a}/{b} TypeError")
except ValueError:
    print(f"code error at: {a}/{b} ValueError")
else:
    print("else statement")
    #print(f"c is: {c}")
finally:
    print("I always run!")

print("If exception is handled, this will be run. If exception is not caught, this will not run.")