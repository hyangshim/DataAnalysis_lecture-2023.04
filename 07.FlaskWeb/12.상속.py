from flask import Flask, render_template


app =Flask(__name__)

#http://localhost:5000/ 입력하면 Hello Flack이 표시됨
@app.route('/')
def index():
    return 'Hello Flack'      # 함수적고 항상 return으로 끝내기

#http://localhost:5000/hello /뒤에는 주소
@app.route('/child1')
def child1():
    return render_template('12.child1.html')
@app.route('/child2')
def child2():
    return render_template('12.child2.html')

if __name__ == '__main__':
    app.run(debug=True)