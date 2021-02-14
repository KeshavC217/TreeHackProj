import requests
from bs4 import BeautifulSoup
import re


def get_descriptions(url, prefix):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_paras = soup.find_all(prefix)
    return [str(i) for i in all_paras]


def isFlower(all_paras):
    p = re.compile('.*flower.*')
    res_list = [s for s in all_paras if p.match(s)]
    if len(res_list) == 0:
        return False
    return True


def getKcal(veg_name):
    veg_arr = veg_name.split(' ')
    veg_name = '_'.join(veg_arr)
    url = 'https://en.wikipedia.org/wiki/' + veg_name
    all_table = get_descriptions(url, "td")
    p = re.compile('.*kcal.*')
    res_list = [s for s in all_table if p.match(s)]
    kcal = res_list[0].split()[2]
    # This will lead to (41 in the case of carrot
    return int(kcal[1:])


