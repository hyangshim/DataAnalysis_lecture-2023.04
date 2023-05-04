from flask import Flask, render_template,request
import os


app =Flask(__name__)

#http://localhost:5000/ 입력하면 Hello Flack이 표시됨
@app.route('/')
def index():
    return 'Hello Flack'      # 함수적고 항상 return으로 끝내기

#http://localhost:5000/hello /뒤에는 주소
@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method =='GET':
        return render_template('14.file.html')
    else:
        file_image =request.files['image']
        filename=os.path.join(app.static_folder,f'upload/{file_image.filename}')
        file_image.save(filename)
        return render_template('14.file_res.html',fname=f'upload/{file_image.filename}')

if __name__ == '__main__':
    app.run(debug=True)