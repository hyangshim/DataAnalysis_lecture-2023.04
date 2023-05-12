from flask import Flask, render_template, request,redirect,session,flash
import melon as melons
import youtube_ranking as you
import Top as To


app =Flask(__name__)

#http://localhost:5000/ 입력하면 Hello Flack이 표시됨
@app.route('/')
def index():
    return 'Hello Flack'      # 함수적고 항상 return으로 끝내기

@app.route('/melon')
def melon():
    melon_list = melons.melon() 
    return render_template('melon.html',melon_list=melon_list)

@app.route('/youtube_ranking')
def youtube():
    youtube_list = you.youtube() 
    return render_template('youtube.html',youtube_list=youtube_list)

@app.route('/TOP20')
def TOP20():
    TOP20_list = To.Top20()
    return render_template('TOP20.html',TOP20_list=TOP20_list)

if __name__ == '__main__':
    app.run(debug=True)

