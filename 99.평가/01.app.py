from flask import Flask, render_template
import pandas as pd
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/melon')
def melon():
    url = 'https://www.melon.com/chart/index.htm'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, 'html.parser')
    trs = soup.select('.service_list_song.type02.d_song_list > table > tbody > tr')
    song_list = []
    for tr in trs:
        rank = tr.select_one('.rank').get_text().strip()
        img = tr.select_one('.image_typeAll > img')['src']
        title = tr.select_one('.ellipsis.rank01 > span > a').get_text().strip()
        artist = tr.select_one('.ellipsis.rank02 > a').get_text().strip()
        album = tr.select_one('.ellipsis.rank03 > a').get_text().strip()
        song_list.append({'순위':rank,'제목':title,'아티스트':artist,'앨범':album,'이미지':img})
    return render_template('01.melon.html', song_list=song_list)

if __name__ == '__main__':
    app.run(debug=True)