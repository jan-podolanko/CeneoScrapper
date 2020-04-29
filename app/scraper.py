#1 import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint
import json
#dodanie funkcji do ekstrakcji
# 'div', 'product-review-summary' 'em'
def extract_feature(opinion, tag, tag_class, child=None):
    try:
        if child:
            return opinion.find(tag, tag_class).find(child).get_text().strip()
        else:
            return opinion.find(tag, tag_class).get_text().strip()
    except AttributeError:
        return None

tags = {
    "recommendation":["div","product-review-summary", "em"],
    "stars":["span", "review-score-count"],
    "content":["p","product-review-body"],
    "author":["div", "reviewer-name-line"],
    "pros":["div", "pros-cell", "ul"],
    "cons":["div", "cons-cell", "ul"], 
    "useful":["button","vote-yes", "span"],
    "useless":["button","vote-no", "span"],
    "purchased":["div", "product-review-pz", "em"]
}
#funkcja do usuwania znakow formatujacucj
def remove_whitespace(string):
    try:
        return string.replace('\n',', ').replace('\r', ', ')
    except AttributeError:
        pass

#2 zdefiniowanie adresu url przykladowej strony z opiniami

url_prefix = 'https://www.ceneo.pl'
product_id = input('Podaj kod produktu: ')
url_postfix = '#tab=reviews'
url = url_prefix + '/' + product_id + url_postfix

opinions_list = []

while url:   
    #3 pobranie kodu html strony z url
    page_response = requests.get(url)
    page_tree = BeautifulSoup(page_response.text, 'html.parser')

    #4 wydobycie z html fragmentow odpowiadajacych poszczegolnym opiniom
    opinions = page_tree.find_all('li', 'js_product-review')

    #pusta lista na wszysykie opinie

    #5 wydobycie skladowych dla pojedynczej opinii
    for opinion in opinions:
        features = {key:extract_feature(opinion, *args)
                    for key, args in tags.items()}
        features["purchased"] = (features["purchased"]=="Opinia potwierdzona zakupem")
        features["opinion_id"] = int(opinion["data-entry-id"])
        features['content'] = remove_whitespace(features['content'])
        dates = opinion.find("span", "review-time").find_all("time")
        features["useful"] = int(features["useful"])
        features["useless"] = int(features["useless"])
        features['pros'] = remove_whitespace(features['pros'])
        features['cons'] = remove_whitespace(features['cons'])
        features["review_date"] = dates.pop(0)["datetime"]
        try:
            features["purchase_date"] = dates.pop(0)["datetime"]
        except IndexError:
            features["purchase_date"] = None

        opinions_list.append(features)

    try:
        url = url_prefix+page_tree.find('a','pagination__next')['href']
    except TypeError:
        url = None
    print(url)

with open("./opinions_json/"+product_id+'.json', 'w', encoding="utf-8") as fp:
    json.dump(opinions_list, fp, ensure_ascii=False, indent=4, separators=(',', ': '))

print(len(opinions_list))