from flask import Flask, render_template ,request


app =Flask(__name__)

#http://localhost:5000/ 입력하면 Hello Flack이 표시됨
@app.route('/')
def index():
    return 'Hello Flack'      # 함수적고 항상 return으로 끝내기

#http://localhost:5000/hello /뒤에는 주소
@app.route('/hello')
def hello():
    return render_template('01.hello.html')

@app.route('/login',methods =['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:                            # method가 POST
        return '환영합니다.'

if __name__ == '__main__':
    app.run(debug=True)