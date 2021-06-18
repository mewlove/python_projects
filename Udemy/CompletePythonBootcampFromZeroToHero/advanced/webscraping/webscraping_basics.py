# (control + '/' for comments)

# To webscrape in python, we can use the BeautifulSoup and requests libraries
# Setup the libraries - type these in the TERMINAL in VS Code or cmd
# pip install requests
# pip install lxml   
# pip install bs4   #BeautifulSoup library
# close VS Code to refresh and when you come back, you should be able to import these libraries e.g import bs4

import requests
import bs4  #type: ignore

############################################################
# GRAB A TITLE
############################################################
print("##########################################")
print(" Grab a Title")
result = requests.get("http://www.example.com") #Get the full html page source in text format
#print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml") #Convert it into a structured BeautifulSoup object, which can grab the info easily
#print(soup)
grab_a_title= soup.select('title') #type:ignore #returns a ResultSet with tags <title ...>
print("Title grabbed: ")
for a in grab_a_title: #type:ignore
    print(a.text) #type:ignore  # text is the text between the tags - e.g <p> ITS THIS TEXT HERE THAT WILL BE RETURNED </p>

print()
grab_a_p = soup.select('p') #type:ignore  #select all paragraph tags <p ...>
print("p grabbed: ")
for a in grab_a_p: #type:ignore
    print(a.text) #type:ignore

############################################################
# GRAB A CLASS
############################################################
# syntax:
# soup.select('div')          All elements with 'div' Tag
# soup.select('#some_id')     Elements containing id='some_id'
# soup.select('.some_class')  Elements containing class='some_class'
# soup.select('div span')     Any elements named span within a div element
# soup.select('div > span')   Any elements named span DIRECTLY within a div element, with nothing in between

print("##########################################")
print(" Grab a Class")
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, "lxml")
content_list = soup.select('.toctext') #type:ignore  #note the dot in front of toctext - (This looks for class = 'toctext')
print(content_list)
print()


############################################################
# GRAB AN IMAGE
############################################################
# e.g <img src='xxxx.jpg'>

print("##########################################")
print(" Grab an Image")

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, "lxml")
content_list = soup.select('img') #type:ignore   #Get all image tags

soup = bs4.BeautifulSoup(res.text, "lxml")
content_list = soup.select('.thumbimage') #type:ignore  #filter the image tags for the important images I want

import os, sys
os.chdir(os.path.abspath(os.path.dirname(sys.argv[0]))) #CHANGE DIR TO THIS FILE LOCATION (for easy file saving)
for a in content_list: #type:ignore
    image_link:str = "https:"+a['src']  #since image links are src='websitename.com/imagelink.jpg', so i append it with https
    #saving to computer:
    image_result = requests.get(image_link) #type:ignore  # I get the image bytes
    #print(image_result.content) 
    f = open('saving_test_image.jpg','wb')  #open a new file as bytes called saving_test_image.jpg
    f.write(image_result.content)           #write the bytes of the image into file
    f.close()
    print("Saving an image...")
print()