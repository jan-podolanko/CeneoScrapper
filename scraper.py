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
opinion = opinions.pop()

opinion_id = opinion["data-entry-id"]
author = opinion.find('div','reviewer-name-line').string
recommendation = opinion.find('div','product-review-summary').find('em').string
stars = opinion.find('span', 'review-score-count').string
purchased = opinion.find('div','product-review-pz').string
useful = opinion.find('button','vote-yes').find('span').string
useless = opinion.find('button','vote-no').find('span').string
content = opinion.find('p','product-review-body').get_text()

#dokoncz daty i pobieraj wszystkie opinie ()