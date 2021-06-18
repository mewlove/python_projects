import one

print("Top level in if_name==main.py")

one.func()

if __name__ == '__main__':
    print("if_name==main.py is being run directly")
else:
    print("if_name==main.py has been imported")