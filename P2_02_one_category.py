#**************************************************************** Import modules
from bs4 import BeautifulSoup
from requests import *
import pandas as pd
import urllib.request
import os
#**************************************************************** Create directories and lists

try:
    os.makedirs('csv/one_category/')
    os.makedirs('images/one_category/')
except OSError:
    pass
else:
    pass

books_links= []
book_info = []
#**************************************************************** Get number of pages of this category

base_url = 'https://books.toscrape.com/catalogue/category/books/childrens_11/index.html'

page_url = (base_url.replace('index.html','')+'page-{}.html')
page_url.format(2)

r = get(base_url)
soup = BeautifulSoup(r.content, "html.parser")
num_of_pages= soup.select_one('ul.pager > li.current').get_text(strip=True)[-1]
p = int(num_of_pages) +1

#**************************************************************** Get all links of all books

for i in range(1,p):
    r = get(page_url.format(i))
    soup = BeautifulSoup(r.content, 'html.parser')
    books = soup.select('div.image_container a')
    
    for link in books:
        all_links = 'https://books.toscrape.com/catalogue/' + link['href'].strip("../")
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
        
#**************************************************************** Extract all books images

    name = "./images/one_category/" + info['universal_ product_code (upc)'] + ".jpg"
    urllib.request.urlretrieve(info['image_url'], name) 

#**************************************************************** With pandas create a dataframe of all books

    book_info.append(info)
df = pd.DataFrame(data = book_info)
df.index +=1
#**************************************************************** Save this dataframe in csv file

df.to_csv('./csv/one_category/'+ info['category']+'.csv', encoding='utf8')  
