# (control + '/' for comments)

def func_turn_range_to_string(n:int):
    return [str(num) for num in range(n)]

def func_turn_range_to_string_using_map(n:int):
    return list(map(str,range(n)))

import time

start_time = time.time()
#RUN CODE
result = func_turn_range_to_string(100000)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
#RUN CODE
result = func_turn_range_to_string_using_map(100000)
end_time = time.time()
print(end_time - start_time)

import timeit
stmt = '''
func_turn_range_to_string(100)
'''
setup = '''
def func_turn_range_to_string(n:int):
    return [str(num) for num in range(n)]
'''

time_function_1 = timeit.timeit(stmt,setup,number=100000)
print(time_function_1)

stmt = '''
func_turn_range_to_string_using_map(100)
'''
setup = '''
def func_turn_range_to_string_using_map(n:int):
    return list(map(str,range(n)))
'''
time_function_2 = timeit.timeit(stmt,setup,number=100000)
print(time_function_2)