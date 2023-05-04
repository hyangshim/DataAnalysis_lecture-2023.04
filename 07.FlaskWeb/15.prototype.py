from flask import Flask, render_template,redirect
from weather_util import get_weather
import 식신 as foods
import park_util as inter
import genie as gn

app =Flask(__name__)


@app.route('/')
def home():
    menu={'ho':1,'us':0,'cr':0,'sc':0}
    return render_template('prototype/home.html', menu=menu)


@app.route('/schedule')
def schedule():
    menu={'ho':0,'us':0,'cr':0,'sc':1}
    num ={'in':0,'in1':1,'in2':0}
    return render_template('prototype/91.schedule.html', menu=menu,weather=get_weather(app))

@app.route('/my')
def my():
    menu={'ho':0,'us':1,'cr':0,'sc':0}
    return render_template('prototype/index0.html',menu=menu)

@app.route('/my1')
def my1():
    menu={'ho':0,'us':1,'cr':0,'sc':0}
    return render_template('prototype/index1.html',menu=menu)

@app.route('/my2')
def my2():
    menu={'ho':0,'us':1,'cr':0,'sc':0}
    return render_template('prototype/index2.html',menu=menu)

@app.route('/food_body')
def food_body():
    food_list =foods.food()
    menu={'ho':0,'us':0,'cr':1,'sc':0}
    return render_template('prototype/food_body.html',menu=menu,food_list=food_list)

@app.route('/interpark')
def interpark():
    menu={'ho':0,'us':0,'cr':1,'sc':0}
    book_list = inter.interpark() 
    return render_template('prototype/interpark.html', book_list=book_list,menu=menu)

@app.route('/genie')
def genie():
    menu={'ho':0,'us':0,'cr':1,'sc':0}
    genie_list = gn.genie() 
    return render_template('prototype/genie.html', genie_list=genie_list,menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
  