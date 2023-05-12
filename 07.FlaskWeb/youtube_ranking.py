import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.parse import quote
import pandas as pd
def convert(s):
    s =s.replace('억','').replace('개','').replace(',','').replace('만','0000')
    return int(s)

def youtube():
    lins =[]
    driver =webdriver.Chrome('file:///C:/Users/YONSAI/Downloads/chromedriver_win32/chromedriver')
    for page  in range(1,11):
        url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=' +str(page)
        driver.get(url)
        time.sleep(2)
        soup =BeautifulSoup(driver.page_source,'html.parser')
        trs =soup.select('.aos-init')

        for tr in trs:
            rank =int(tr.select_one('.info_rank').get_text().strip())
            category=tr.select_one('.category').get_text().strip()[1:-1]
            title = tr.select_one('.subject > h1 > a').get_text().strip()
            subscriber = convert(tr.select_one('.subscriber_cnt').get_text().strip())
            view = convert(tr.select_one('.view_cnt').get_text().strip())
            video = convert(tr.select_one('.video_cnt').get_text().strip())
            lins.append({'순위':rank,'카테고리':category,'채널명':title,'구독자수':subscriber,
                        '조회수':view,'비디오':video})
    driver.close()
    return lins