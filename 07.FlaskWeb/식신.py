import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import pandas as pd
def food():
    base_url ='https://www.siksinhot.com/search'
    url =f'{base_url}?keywords={quote("장안문")}'
    result =requests.get(url)
    html = result.text
    soup=BeautifulSoup(result.text,'html.parser')
    lis = soup.select_one('.localFood_list').find_all('li')
    line = [ ]
    for li in lis:
        img = li.find('img')['src']
        href = li.find('a')['href']
        title=li.select_one('.textBox > h2').get_text()
        score = li.select_one('.textBox > .score').get_text()
        atags =li.select('.cate >a')
        location = atags[0].get_text()
        menu = atags[1].get_text()
        line.append({'img':img,'제목':title,'점수':score,'위치':location,'메뉴':menu,'href':base_url+href})
    return line