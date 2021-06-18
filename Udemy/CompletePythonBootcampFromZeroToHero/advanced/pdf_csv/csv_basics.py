# (control + '/' for comments)


################################################
# CSV Stands for comma separated variables
################################################
import os, sys
os.chdir(os.path.dirname(sys.argv[0]))
print(f"cwd: {os.getcwd()}")



##############################################################################################
# OPEN A FILE AND READ WHAT IS INSIDE
##############################################################################################
import csv

data = open('example.csv',encoding='utf-8')
csv_data = csv.reader(data)

#reformat it to a python object list of lists
data_lines = list(csv_data)
for line in data_lines:
    pass
    #print(line)

full_names:list[str] = []
for line in data_lines[1:]:
    full_names.append(line[1]+" "+line[2])
#print(full_names)


##############################################################################################
# OPEN A NEW FILE AND WRITE TO IT
##############################################################################################
file_to_output = open('to_save_file.csv',mode='w', newline='')  #mode ='w' is to write a new file
csv_writer = csv.writer(file_to_output,delimiter=',')  #Note: delimiter is specified

row1 = ['a','b','c','d']
row2 = ['1','2','3','4']
row3 = ['5','6','7','8']
row4 = ['9','10','11','12']

csv_writer.writerow(row1)
csv_writer.writerows([row2,row3])
file_to_output.close()


##############################################################################################
# OPEN AND APPEND
##############################################################################################
f = open('to_save_file.csv',mode='a',newline='')  #mode='a' is to append to an existing file
csv_writer = csv.writer(f) #Note: delimiter does not need to be specified
csv_writer.writerow(row4)
f.close()
