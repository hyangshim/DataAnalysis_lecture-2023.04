from flask import Flask, render_template


app =Flask(__name__)

#http://localhost:5000/ 입력하면 Hello Flack이 표시됨
@app.route('/')
def index():
    return 'Hello Flack'      # 함수적고 항상 return으로 끝내기

#http://localhost:5000/hello /뒤에는 주소
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):         #name 값을 주면 그값으로 되고,안주면 None이됨
    dt ={'key1':'value1','key2':'value2','key3':'value3'}
    return render_template('06.hello.html',name=name,dt=dt,item='item')

if __name__ == '__main__':
    app.run(debug=True)