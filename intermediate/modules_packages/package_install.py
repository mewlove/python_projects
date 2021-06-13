# (control + '/' for comments)

# JUST A TEXT FILE
'''
Type this in command line:
pip install [package_name]

example: pip install requests
example: pip install colorama
example: pip install openpyxl
'''

#after installing, it can be used!
from openpyxl import Workbook
wb = Workbook()

ws = wb.active
ws['A1'] = 10
ws.append([1,2,3])

wb.save('test.xlsx')
