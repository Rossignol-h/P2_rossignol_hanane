
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
#### The following directories will be automatically created 

#### For one book scraped :
#### 1 image and 1 csv file will be added in:

```bash
  images/one_book/
```
```bash
 csv/one_book/
```
#### For one category scraped
#### all images of this category and 1 csv file will be added in:
```bash
  images/one_category/
```
```bash
 csv/one_category/
 ```
#### For all books scraped
#### 1000 images and 50 csv files (1 csv/category) will be added in:
```bash
  images/all_categories/
```
```bash
 csv/all_categories/
## Author

- Rossignol Hanane [@Rossignol-h](https://github.com/Rossignol-h)

