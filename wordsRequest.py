import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import json

ua = UserAgent()
headers_r = {'User-Agent':str(ua.chrome)}

def words_Russian(letter):
    words = []
    for i in range(1,20):
        ojigov_url = f'https://ozhegov.slovaronline.com/articles/{letter}/page-{i}'
        r = requests.get(ojigov_url, headers=headers_r)
        print(r.status_code)
        if r.status_code != 200:
            break
        soup = BeautifulSoup(r.text, 'lxml')
        words_title = soup.find('div', {'class': 'articles-link-list'})
        for i in words_title.find_all('a'):
            if i.text[-1] == '.':
                continue
            words.append(i.text.replace('\ufeff', ''))
        time.sleep(5.5)
    return words

def words_add(letter):
    words = words_Russian(letter)
    words_add_json = {f'{letter}': words}
    with open('words_Russian.json', 'r') as file:
        words_Russian_data = json.load(file)
        new_words = {**words_Russian_data, **words_add_json}
    with open('words_Russian.json', 'w') as file:
        json.dump(new_words, file, indent='', ensure_ascii=False)
Russian_alpabet = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'

for i in Russian_alpabet:
    print(i)
    words_add(i)
    time.sleep(5.5)