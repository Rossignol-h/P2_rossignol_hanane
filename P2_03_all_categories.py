#**************************************************************** Import modules
from bs4 import BeautifulSoup
from requests import *
import pandas as pd
import urllib.request
import os
#**************************************************************** Create directories and lists

books_links= []
book_info = []

try:
   os.makedirs('csv/all_categories/')
   os.makedirs('images/all_categories/')
except OSError:
   pass
else:
   pass
#**************************************************************** Get 50 links of all website pages

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
base_url.format(2)

for i in range(1,2): 
    r = get(base_url.format(i))
    soup = BeautifulSoup(r.text, 'html.parser')
    tags = soup.select('div.image_container a')
#**************************************************************** Get 1000 links of all books

    for a in tags:
        all_links = 'https://books.toscrape.com/catalogue/' + a['href']
        books_links.append(all_links)      
#**************************************************************** Extract data of each book

for link in books_links:
    r = get(link)
    soup = BeautifulSoup(r.content,'html.parser')
    table = soup.select("td")

    info = {}
    info['title']= soup.select_one("h1").text
    info['category']= soup.select('.breadcrumb > li > a')[-1].text
    info['universal_ product_code (upc)']= table[0].text
    info['price_including_tax']= table[3].text
    info['price_excluding_tax']= table[2].text
    info['number_available']= table[5].text.strip("In stock (available)")
    info['review_rating']= soup.select('p.star-rating')[0].get('class')[1]
    info['product_page_url']= link
    info['image_url']= 'http://books.toscrape.com/' + soup.select_one('.carousel-inner > .item > img')['src'].strip("../")
    try:
        info['product_description']= soup.select_one('#product_description + p').text
    except AttributeError as err:
        info['product_description']= None
#**************************************************************** Extract all 1000 books images
    
    name = "./images/all_categories/" + info['universal_ product_code (upc)'] + ".jpg"
    urllib.request.urlretrieve(info['image_url'], name)

#**************************************************************** With pandas create a dataframe of all books
    book_info.append(info)
df = pd.DataFrame(book_info)
#**************************************************************** and slice it for each category

df_by_category = df.groupby('category')

#**************************************************************** Save in 50 csv files (1/category) 

for k, gr in df_by_category:
    gr.to_csv('./csv/all_categories/{}.csv'.format(k), encoding='utf8')