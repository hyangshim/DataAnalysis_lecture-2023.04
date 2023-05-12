import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import pandas as pd

def melon():
    url = "https://www.melon.com/chart/index.htm"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text)
    trs = soup.select('tr.lst50,tr.lst100')
    tr =trs[0]
    lin =[]
    for tr in trs:
        rank=tr.select_one('.rank').get_text()
        title =tr.select_one('span> a').get_text().split('\n')[-1].strip()
        arist=tr.select_one('.ellipsis >a').get_text()
        album =tr.select_one('.ellipsis.rank03').get_text().strip()
        img = tr.select_one('.image_typeAll > img')['src']
        lin.append({'순위':rank,'제목':title,'아티스트':arist,'앨범':album,'이미지':img})
    return lin