from flask import Flask, render_template
import os


app =Flask(__name__)

#http://localhost:5000/ 입력하면 Hello Flack이 표시됨
@app.route('/')
def index():
    return 'Hello Flack'      # 함수적고 항상 return으로 끝내기

#http://localhost:5000/hello /뒤에는 주소
@app.route('/static_resource')
def static_resource():
    #static resource가 Cache로 인해서 즉시 변경이 일어나지 않을 경우
    image_file = os.path.join(app.root_path,'static/img/고양이.jpg')
    mtime =int(os.stat(image_file).st_mtime)    #마지막으로 변경된시간
    return render_template('05.static.html',mtime =mtime)

if __name__ == '__main__':
    app.run(debug=True)