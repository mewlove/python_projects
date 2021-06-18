# (control + '/' for comments)


################################################
# PDF stands for Portable Document Format
# Will be using PyPDF2 in this file
# PyPDF May not be able to read all PDF files
# This is due to the fact that there are no
# standards for a PDF file

#NOTES: https://pythonhosted.org/PyPDF2/PageObject.html

#
# SETUP:
# pip install PyPDF2
################################################

#Change directory to same as this file
import os, sys
os.chdir(os.path.dirname(sys.argv[0]))
print(f"cwd: {os.getcwd()}")



##############################################################################################
# OPEN A FILE AND READ WHAT IS INSIDE
##############################################################################################
import PyPDF2 #type:ignore

working_business_proposal_pdf = "Working_Business_Proposal.pdf"
some_BrandNew_Doc_pdf = "Some_BrandNew_Doc.pdf"
some_New_Doc_pdf = "Some_New_Doc.pdf"
some_new_file_pdf = "Some_new_file.pdf"

f = open(working_business_proposal_pdf,'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(f"Num of pages: {pdf_reader.numPages}")

page_one = pdf_reader.getPage(0) #type:ignore
page_one_text = page_one.extractText()  #type:ignore
# print(page_one_text)  #type:ignore

f.close()




##############################################################################################
# COPY PART OF A FILE AND WRITE IT TO A NEW FILE
##############################################################################################
f = open(working_business_proposal_pdf,'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page: PyPDF2.pdf.PageObject = pdf_reader.getPage(0) #type:ignore

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page) #type:ignore

pdf_output = open(some_BrandNew_Doc_pdf,'wb')
pdf_writer.write(pdf_output)  #type:ignore
f.close()





##############################################################################################
# 
##############################################################################################

f = open (working_business_proposal_pdf,'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

#Go through all its pages:
pdf_text = []
for page_no in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_no)   #type:ignore
    pdf_text.append(page.extractText())  #type:ignore

print(pdf_text)   #type:ignore

