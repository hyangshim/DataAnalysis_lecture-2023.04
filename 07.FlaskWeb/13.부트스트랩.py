from flask import Flask, render_template
import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template,request
import map_util as mu
import park_util as inter

app =Flask(__name__)

#http://localhost:5000/ 입력하면 Hello Flack이 표시됨
@app.route('/')
def index():
    return 'Hello Flack'      # 함수적고 항상 return으로 끝내기

#http://localhost:5000/hello /뒤에는 주소
@app.route('/carousel')
def carousel():
    return render_template('13.Carousel.html')
@app.route('/Progress')
def Progress():
    return render_template('13.Progress Bars.html')

@app.route('/scatter',methods =['GET','POST'])
def scatter():
    if request.method == 'GET':
        return render_template('09.산점도.html')
    else:
        num =int(request.form['num'])
        mean =float(request.form['mean'])
        std =float(request.form['std'])
        min =float(request.form['min'])
        max =float(request.form['max'])
        xs =np.random.normal(loc=mean, scale=std,size=num)
        ys =np.random.uniform(min,max,num)
        plt.figure()
        plt.scatter(xs,ys)
        filename =os.path.join(app.static_folder,'img/scatter.png')
        plt.savefig(filename)
        return render_template('09.산점도_res.html')
    
@app.route('/hotplaces',methods =['GET','POST'])
def hotplaces():
    if request.method == 'GET':
        return render_template('10.Hotplaces.html')
    else:
        #client가 입력한 장소 알아내기
        place1=request.form['place1']
        place2=request.form['place2']
        place3=request.form['place3']
        places=[place1,place2,place3]
        mu.hot_places(places,app)
        return render_template('10.Hotplaces_res.html')
    
@app.route('/interpark')
def interpark():
    book_list = inter.interpark() 
    return render_template('11.interpark.html', book_list=book_list)

if __name__ == '__main__':
    app.run(debug=True)