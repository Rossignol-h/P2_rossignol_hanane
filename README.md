
# Project 2 - Scraping Books

This project is a scraper for books.toscrape.com website


## Installation

clone repository locally

```bash
git clone https://github.com/Rossignol-h/P2_rossignol_hanane.git
```
Create a virtual environment in root folder of project

```bash
python -m venv env
```
Activate virtual environment
```bash
env/Script/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
## Usage & Examples

#### For scraping one book open this file :
```python
P2_01_one_book.py
```
Paste the url of the chosen book in : base_url
```python
base_url = 'https://books.toscrape.com/catalogue/the-requiem-red_995/index.html'
```
```python
run the script
```

#### For scraping one category open this file :
```python
P2_02_one_category.py
```
Paste the url of the wanted category in base_url
```python
base_url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
```
```python
run the script
```
#### For scraping all books of the website run this file :
```python
python P2_03_all_categories.py
```
## Results 
### *Note: The following directories will be automatically created when you run each scripts*
***
#### For one book scraped :

```bash
# 1 image [ *with "unique number UPC" of the book as name* ]
  images/one_book/f77dbf2323deb740.jpg
```

```bash
# 1 csv file [ *with "unique number UPC" of the book as name* ]
 csv/one_book/f77dbf2323deb740.csv
```

***
#### **For one category scraped :**

```bash
# all images of this category [ with "unique number UPC" of the book as name ]
  images/one_category/a22124811bfa8350.jpg...
```

```bash
# 1 csv file [ with the category as name ]
 csv/one_category/Travel.csv
 ```

***
#### **For all books scraped :**
 

```bash
# 1000 images [ with "unique number UPC" of the book as name ]
  images/all_categories/a22124811bfa8350.jpg...
```
```bash
# 50 csv files [ with the category as name ] (1 csv/category)
 csv/all_categories/Travel.csv Art.csv Crime.csv...
```

***
## Author

- Rossignol Hanane 
- Github Profile :octocat: [@Rossignol-h](https://github.com/Rossignol-h)

