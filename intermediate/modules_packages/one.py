#one.py

'''
THIS PYTHON SCRIPT IS ONLY USED BY ANOTHER SCRIPT AS AN EXAMPLE OF WHY __name__ == '__main__' is used!!!
Please visit if_name==main.py to see its usage
'''

def func():
    print("func() in one.py")

print("Top level in one.py")

if __name__ == '__main__':
    print("one.py is being run directly")
else:
    print("one.py has been imported")