import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template,request


app =Flask(__name__)

#http://localhost:5000/ 입력하면 Hello Flack이 표시됨
@app.route('/')
def index():
    return 'Hello Flack'      # 함수적고 항상 return으로 끝내기

#http://localhost:5000/hello /뒤에는 주소
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

if __name__ == '__main__':
    app.run(debug=True)