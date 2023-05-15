from flask import Flask, render_template, request
import youtube_util as yu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/youtube_ranking', methods=['GET','POST'])
def youtube_ranking():
    if request.method == 'GET':
        return render_template('02.spinner.html')
    else:
        channel_list = yu.get_youtube_list()
        return render_template('02.youtube.html', channel_list=channel_list)

@app.route('/top20_subscriber')
def top20_subscriber():
    yu.top20_subscriber()
    return render_template('02.subscriber.html')

@app.route('/top20_view')
def top20_view():
    yu.top20_view()
    return render_template('02.view.html')

@app.route('/top10_category')
def top10_category():
    yu.top10_category()
    return render_template('02.category.html')

if __name__ == '__main__':
    app.run(debug=True)