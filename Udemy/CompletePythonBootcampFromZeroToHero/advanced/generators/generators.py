# (control + '/' for comments)

def create_cubes_basic(n:int):
    result = [x**3 for x in range(0,n)]  # list comprehension
    return result

def create_cubes(n:int):
    for x in range(n):
        yield x**3

for i in create_cubes(5):
    print(i)

def gen_fibonacci(n:int):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        a,b = b, a+b

print("saving a generator")
g_fib = gen_fibonacci(100)

print(next(g_fib))
print(next(g_fib))
print(next(g_fib))
print(next(g_fib))
print(next(g_fib))
print(next(g_fib))


def create_cubes_gencom(n:int):
    return (x**3 for x in range(n))  # returns a generator comprehension -- notice the brackets

print("Creates a generator comprehension")
gcom = create_cubes_gencom(100)
print(next(gcom))
print(next(gcom))
print(next(gcom))