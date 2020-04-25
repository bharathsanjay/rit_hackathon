#Image extraction module still in testing

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import itertools
import requests
import json

def get_soup(url):
    """REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}"""
    response = requests.get(url,params = keyword)
    return BeautifulSoup(response.text, 'html.parser')

def imgextract(keyword):
    keyword = keyword.split()
    keyword ='+'.join(keyword)
    url="http://www.bing.com/images/search?q="+keyword
    soup = get_soup(url)
    print(soup)
    #t = soup.find_all("div",{"class":"rg_meta"})
    soup_imgs = soup.find('a', attrs={'class':'iusc'})
    for i in soup_imgs:
        src = i['src']
        return src
    

