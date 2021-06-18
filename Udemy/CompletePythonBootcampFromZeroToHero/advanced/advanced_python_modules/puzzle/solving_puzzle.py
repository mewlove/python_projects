# (control + '/' for comments)
import os, sys

file_path = sys.argv[0]            
pathname = os.path.abspath(os.path.dirname(sys.argv[0]))
os.chdir(pathname)

import shutil
provided_zip = 'unzip_me_for_instructions.zip'
unzipped_folder_name = 'unzipped_folder'
shutil.unpack_archive(provided_zip,unzipped_folder_name,'zip')

import re
def search_full_dir(path_dir:str, regex_str:str):
    search_str:list[str] = []
    tab_str = '|\t'
    def recursive_print(path_dir:str, prefix:str):
        all_files_in_dir = os.listdir(path_dir)
        for f in all_files_in_dir:
            print(prefix+f)
            if(os.path.isdir(path_dir+"\\"+f)):
                recursive_print(path_dir+"\\"+f,prefix+tab_str)
            else:
                with open(path_dir+"\\"+f,mode='r') as myfile:
                    contents = myfile.read()
                    matches = re.findall(regex_str,contents)
                    search_str.extend(list(matches))
    recursive_print(path_dir,"")
    return search_str

def walkthrough_path(path_dir:str, regex_str:str):
    search_str:list[str] = []
    for folder, _, files in os.walk(path_dir):
        for f in files:
            print("Open: "+folder+"\\"+f)
            with open(folder+"\\"+f,mode='r') as myfile:
                    contents = myfile.read()
                    matches = re.findall(regex_str,contents)
                    search_str.extend(list(matches))
        # for sf in subfolders:
        #     print(path_dir+"\\"+sf)
        #     search_str.extend(walkthrough_path(path_dir+"\\"+sf, regex_str))
    return search_str

print("All paths:")
unzipped_folder_path = os.getcwd()+"\\"+unzipped_folder_name

with open(unzipped_folder_path+"\\Extracted_content\\Instructions.txt",mode='r') as myfile:
    contents = myfile.read()
    print(contents)

pattern = r"\d{3}-\d{3}-\d{4}"
list_of_numbers = search_full_dir(unzipped_folder_path,pattern)
print(list_of_numbers)

list_of_numbers = walkthrough_path(unzipped_folder_path+"\\extracted_content",pattern)
print(list_of_numbers)