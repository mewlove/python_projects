# (control + '/' for comments)

#   Website specifically for people to practice webscraping: 
#       http://toscrape.com
#


import requests, bs4 #type: ignore
############################################################
# GOAL is to get the title of books with two star ratings
############################################################
base_url = "http://books.toscrape.com/catalogue/page-{}.html" #the website we are gonna be scraping... note there is a {} for formatting
two_star_rating = '.star-rating.Two' #the name of the class for two star rating books
three_star_rating = '.star-rating.Three' #can be substituted with two_star_rating above to differentiate the results
total_number_of_pages = 50 #manually checked on the webpage

for i in range(1,total_number_of_pages+1): #inclusive of low, exclusive of high
    res = requests.get(base_url.format(i)) #go through all pages from /page-1.html to /page-50.html
    soup = bs4.BeautifulSoup(res.text,"lxml")
    product_list = soup.select('.product_pod')  #type: ignore  #product_pod seems to be the class of each object item
    for p in product_list: #type:ignore  #go through each object item
        if len(p.select(two_star_rating)) != 0: #type: ignore       #check if star rating is two
            print(p.select('a')[1]['title'])  #type: ignore     #print all the titles of books with star rating two