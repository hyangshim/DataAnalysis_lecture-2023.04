from flask import Flask, render_template, request
import graph_util as gu
import map_util as mu
import crawl_util as cu

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homework/home.html')

@app.route('/scatter', methods=['GET','POST'])
def scatter():
    if request.method == 'GET':
        return render_template('homework/scatter.html')
    else:
        num = int(request.form['num'])
        mean = float(request.form['mean'])
        std = float(request.form['std'])
        min = float(request.form['min'])
        max = float(request.form['max'])
        gu.scatter(num, mean, std, min, max, app)
        return render_template('homework/scatter_res.html')

@app.route('/hotPlaces', methods=['GET','POST'])
def hot_places():
    if request.method == 'GET':
        return render_template('homework/hot_places.html')
    else:
        # client가 입력한 장소 알아내기
        place1 = request.form['place1']
        place2 = request.form['place2']
        place3 = request.form['place3']
        places = [place1, place2, place3]
        mu.hot_places(places, app)
        return render_template('homework/hot_places_res.html')

@app.route('/interpark')
def interpark():
    book_list = cu.interpark()
    return render_template('homework/interpark.html', book_list=book_list)

@app.route('/progress')
def progress():
    return render_template('homework/progress_bar.html')

if __name__ == '__main__':
    app.run(debug=True)
