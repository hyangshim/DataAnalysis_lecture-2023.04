from flask import Flask, render_template,request
import map_util as mu


app =Flask(__name__)

#http://localhost:5000/ 입력하면 Hello Flack이 표시됨
@app.route('/')
def index():
    return 'Hello Flack'      # 함수적고 항상 return으로 끝내기

#http://localhost:5000/hello /뒤에는 주소
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
    
if __name__ == '__main__':
    app.run(debug=True)