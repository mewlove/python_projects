# (control + '/' for comments)
import os, sys

print("Starting working directory: "+os.getcwd())

file_path = sys.argv[0]            
pathname = os.path.abspath(os.path.dirname(sys.argv[0]))
os.chdir(pathname)
print("Current working directory: "+os.getcwd())


f = open('fileone.txt','w+')
f.write('File ONE')
f.close()


f = open('filetwo.txt','w+')
f.write('File TWO')
f.close()

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')

zip_obj.extractall('extracted_content')


import shutil

dir_to_zip = "extracted_content"
output_filename = 'example_zip_folder'
shutil.make_archive(output_filename,'zip',dir_to_zip)

shutil.unpack_archive('example_zip_folder.zip','shutil_unzip','zip')
