import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

def interpark():
    base_url = 'http://book.interpark.com'
    sub_url = '/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028'
    res = requests.get(base_url + sub_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    lis = soup.select('.rankBestContentList > ol > li')
    lines = []
    for li in lis:
        img = li.select_one('.coverImage').find('img')['src']
        href = li.select_one('.coverImage').find('a')['href']
        rank_data = li.select('.rankBtn_ctrl')
        if len(rank_data) == 1:
            rank = int(rank_data[0]['class'][-1][-1])
        else:
            rank = int(rank_data[0]['class'][-1][-1] + rank_data[1]['class'][-1][-1]) 
        title = li.select_one('.itemName').get_text().strip()
        author = li.select_one('.author').get_text().strip()
        company = li.select_one('.company').get_text().strip()
        price = li.select_one('.price > em').get_text().strip()   
        lines.append({'순위':rank, '제목':title, '저자':author, '출판사':company, 
                      '가격':price, 'img':img, 'href':base_url+href})
    return lines

def genie():
    url = 'https://www.genie.co.kr/chart/top200'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, 'html.parser')
    trs = soup.select('tr.list')
    lines = []
    for tr in trs:
        rank = tr.select_one('.number').get_text().split('\n')[0].strip()
        img = 'https:' + tr.select_one('.cover > img')['src']
        title = tr.select_one('.title.ellipsis').get_text().split('\n')[-1].strip()
        artist = tr.select_one('.artist.ellipsis').string.strip()
        album = tr.select_one('.albumtitle.ellipsis').text.strip()
        lines.append({'rank':rank, 'img':img, 'title':title, 'artist':artist, 'album':album}) 
    return lines

def siksin(place):
    base_url = 'https://www.siksinhot.com/search'
    url = f'{base_url}?keywords={quote(place)}'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    lis = soup.select('.localFood_list > li')
    lines = []
    for li in lis:
        img = li.find('img')['src']
        title = li.select_one('.textBox > h2').get_text()
        score = li.select_one('.textBox > .score').get_text()
        atags = li.select('.cate > a')
        location = atags[0].get_text()
        menu = atags[1].get_text()
        lines.append({'img':img, 'title':title, 'score':score, 'location':location, 'menu':menu})
    return lines