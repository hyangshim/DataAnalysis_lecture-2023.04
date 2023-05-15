import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import seaborn as sns
import matplotlib.pyplot as plt

def convert(s):
    s = s.replace('억','').replace('개','').replace(',','').replace('만','0000')
    return int(s)

def get_youtube_list():
    lines = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')   # 화면없이 실행
    options.add_argument('--no-sandbox')
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome('C:/Users/YONSAI/Downloads/chromedriver.exe', options=options)
    for page in range(1, 11):
        url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=' + str(page)
        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        trs = soup.select('.aos-init')

        for tr in trs:
            rank = int(tr.select_one('.rank').get_text().strip())
            category = tr.select_one('.category').get_text().strip()[1:-1]
            channel = tr.select_one('.subject > h1 > a').get_text().strip()
            subscriber = convert(tr.select_one('.subscriber_cnt').get_text().strip())
            view = convert(tr.select_one('.view_cnt').get_text().strip())
            video = convert(tr.select_one('.video_cnt').get_text().strip())
            lines.append({
                '순위':rank, '카테고리':category, '채널명':channel,
                '구독자수':subscriber, '조회수':view, '비디오수':video
            })
    df = pd.DataFrame(lines)
    df.to_csv('static/YouTube랭킹.csv', index=False)
    driver.close()  
    return lines

def top20_subscriber():
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    df = pd.read_csv('static/YouTube랭킹.csv')
    df1 = df.sort_values(by='구독자수', ascending=False)

    plt.figure(figsize=(12,8))
    sns.barplot(y='채널명', x='구독자수', data=df1.head(20))
    plt.title('구독자수 Top 20 채널')
    plt.savefig('static/top20_subscriber.png')

def top20_view():
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    df = pd.read_csv('static/YouTube랭킹.csv')
    df1 = df.sort_values(by='조회수', ascending=False)

    plt.figure(figsize=(12,8))
    sns.barplot(y='채널명', x='조회수', data=df1.head(20))
    plt.title('조회수 Top 20 채널')
    plt.savefig('static/top20_view.png')

def top10_category():
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    df = pd.read_csv('static/YouTube랭킹.csv')
    df3 = df.카테고리.value_counts().to_frame()

    plt.figure(figsize=(12,5))
    sns.barplot(y=df3.index[:10], x='count', data=df3.head(10))
    plt.title('카테고리별 채널수 Top 10')
    plt.savefig('static/top10_category.png')