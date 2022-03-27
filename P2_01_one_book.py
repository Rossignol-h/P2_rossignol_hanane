#**************************************************************** Import modules
from bs4 import BeautifulSoup
from requests import *
import pandas as pd
import urllib.request
import os
#**************************************************************** Create directories for images ans csv files

try:
   os.makedirs('./csv/one_book')
   os.makedirs('./images/one_book')
except OSError as error:
   print(error)
else:
   pass
#**************************************************************** Get page content and parse it

base_url = 'https://books.toscrape.com/catalogue/the-requiem-red_995/index.html'
r = get(base_url).content
soup = BeautifulSoup(r,'html.parser')
table = soup.select("td")

#**************************************************************** Extract book data
info = {}
info['title']= soup.select_one("h1").text
info['category']= soup.select('.breadcrumb > li > a')[-1].text
info['universal_ product_code (upc)']= table[0].text
info['price_including_tax']= table[3].text
info['price_excluding_tax']= table[2].text
info['number_available']= table[5].text.strip("In stock (available)")
info['review_rating']= soup.select('p.star-rating')[0].get('class')[1]
info['product_page_url']= base_url
info['image_url']= 'http://books.toscrape.com/' + soup.select_one('.carousel-inner > .item > img')['src'].strip("../")
try:
   info['product_description']= soup.select_one('#product_description + p').text
except AttributeError as err:
   info['product_description']= None
#**************************************************************** Extract book image

name = "./images/one_book/" + info['universal_ product_code (upc)'] + ".jpg"
urllib.request.urlretrieve(info['image_url'], name) 
#**************************************************************** With pandas create a dataframe

df = pd.DataFrame.from_dict(data = info, orient='index')
df = df.transpose()
#**************************************************************** Save this dataframe in csv file

df.to_csv('./csv/one_book/'+ info['universal_ product_code (upc)'] +'.csv', index=False, encoding='utf8')