#import bibliotek
import os

#wyswietlanie zawartosci katalogu z opiniami (.json)
print(*os.listdir("./opinions_json"))

#wczytanie identyfikatora produktuu ktorego opinie beda analizowane
product_id = input('Podaj kod produktu: ')

#wczytanie do ramki danych opinii z pliku 
opinions = pd.read_json('./opinions_json/'+product_id+'.json')
opinions = opinions.set_index('opinion_id')

print(opinions)