import requests
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