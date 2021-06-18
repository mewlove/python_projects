# (control + '/' for comments)

import os

print("Current Working dir:")
print(os.getcwd())
print("List dir:")
print(os.listdir())
print("List dir (dir for this file):")
print(os.listdir(os.getcwd()+"\\advanced\\advanced_modules"))

print()
print("import shutil")
import shutil

print("move file")
if("practice.txt" in os.listdir()):
    print(shutil.move('practice.txt',os.getcwd()+"\\advanced"))
elif("practice.txt" in os.listdir(os.getcwd()+"\\advanced")):
    print(shutil.move(os.getcwd()+"\\advanced\\"+'practice.txt',os.getcwd()))

#delete files (Try to use send2trash instead of os.unlink(path) or os.rmdir() or shutil.rmtree)
#all the above delete file will permanently delete files so if delete wrong files
#cannot be reversed
#Use send2trash instead
#pip install send2trash
#import send2trash
#send2trash.send2trash('practice.txt')

print(f"os.walk(\"{os.getcwd()}\\advanced\")")
dir_gen = os.walk(os.getcwd()+"\\advanced")
for i in dir_gen:
    print(i)

print()
print(f"os.walk(\"{os.getcwd()}\\advanced\"): Clearer version")
dir_gen = os.walk(os.getcwd()+"\\advanced")
for folder, subfolder, files in dir_gen:
    print("---")
    print(f"Folder: {folder}")
    print(f"\tSubfolder: {subfolder}")
    print(f"\tFile: {files}")