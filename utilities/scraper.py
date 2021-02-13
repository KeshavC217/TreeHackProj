import requests
from bs4 import BeautifulSoup
import re


def get_descriptions(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_paras = soup.find_all("p")
    return [str(i) for i in all_paras]


def isFlower(all_paras):
    p = re.compile('.*flower.*')
    res_list = [s for s in all_paras if p.match(s)]
    if len(res_list) == 0:
        return False
    return True

url='https://en.wikipedia.org/wiki/Quercus_alba'
print(isFlower(get_descriptions(url)))
