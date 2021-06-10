# # READ WRITE
# mode = 'r' - read only
# mode = 'w' - write only (overwrite or create new files)
# mode = 'a' - append only (add on to existing file)
# mode = 'r+' - reading and writing
# mode = 'w+' - writing and reading (overwrite or create new files)
# (control + '/' for comments)

# using the with/as statement, there is no need to call myfile.close() as myfile will
# automatically be closed after program is done
with open('test.txt',mode='w') as myfile:
    myfile.write('Gonna start a new file\n')
    myfile.write('Second line\n')
    myfile.write('Third line\n')

print("\n")
with open('test.txt',mode='r') as myfile:
    contents = myfile.read()

print(f"with open('test.txt',mode='r') as myfile:\ncontents = myfile.read()\n--contents:\n{contents}")


with open('test.txt',mode='r') as myfile:
    contents = myfile.readlines()
   
print(f"with open('test.txt',mode='r') as myfile:\ncontents = myfile.readlines()\n--contents:\n{contents}")