#1 import bibliotek
import requests
from bs4 import BeautifulSoup

#2 zdefiniowanie adresu url przykladowej strony z opiniami

url = 'https://www.ceneo.pl/84507187#tab=reviews'


#3 pobranie kodu html strony z url
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')

#4 wydobycie z html fragmentow odpowiadajacych poszczegolnym opiniom
opinions = page_tree.find_all('li', 'review-box')

#5 wydobycie skladowych dla pojedynczej opinii
for opinion in opinions:
    opinion_id = opinion["data-entry-id"]
    author = opinion.find('div','reviewer-name-line').string
    recommendation = opinion.find('div','product-review-summary').find('em').string
    stars = opinion.find('span', 'review-score-count').string
    try:
        purchased = opinion.find('div','product-review-pz').string
    except AttributeError:
        purchased = None
    useful = opinion.find('button','vote-yes').find('span').string
    useless = opinion.find('button','vote-no').find('span').string
    content = opinion.find('p','product-review-body').get_text()
    dates = opinion.find('span','review-time').find_all('time')
    review_date = dates.pop(0)['datetime']
    try:
        purchase_date = dates.pop(0)['datetime']
    except AttributeError:
        purchase_date = None
    try:
        pros = opinion.find('div','pros-cell').find('ul').get_text()
    except AttributeError:
        pros = None
    try:
        cons = opinion.find('div','cons-cell').find('ul').get_text()
    except AttributeError:
        cons = None
        
#zrobic to do wszystkich opinii