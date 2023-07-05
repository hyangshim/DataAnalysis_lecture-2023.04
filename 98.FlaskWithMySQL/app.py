from flask import Flask, render_template, request, redirect
import db.kpop_dao as kd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('00.hello.html')

@app.route('/song/list')
def song_list():
    songs = kd.get_song_list(20)
    return render_template('01.song_list.html', songs=songs)

@app.route('/song/add', methods=['GET', 'POST'])
def song_add():
    if request.method == 'GET':
        return render_template('02.song_add.html')
    else:
        title = request.form['title']
        lyrics = request.form['lyrics']
        kd.insert_song((title, lyrics))
        return redirect('/song/list')
    
@app.route('/song/update/<sid>', methods=['GET', 'POST'])
def song_update(sid):
    if request.method == 'GET':
        song = kd.get_song(sid)
        return render_template('03.song_update.html', song=song)
    else:
        title = request.form['title']
        lyrics = request.form['lyrics']
        kd.update_song((title, lyrics, sid))
        return redirect('/song/list')
    
@app.route('/song/delete/<sid>')
def song_delete(sid):
    kd.delete_song(sid)
    return redirect('/song/list')

@app.route('/gg/list')
def gg_list():
    groups = kd.get_girl_group_list(20)
    return render_template('11.gg_list.html', groups=groups)

@app.route('/gg/add', methods=['GET', 'POST'])
def gg_add():
    if request.method == 'GET':
        return render_template('12.gg_add.html')
    else:
        name = request.form['name']
        debut = request.form['debut']
        hid = request.form['hid']
        kd.insert_girl_group((name, debut, hid))
        return redirect('/gg/list')
    
@app.route('/gg/update/<gid>', methods=['GET', 'POST'])
def gg_update(gid):
    if request.method == 'GET':
        group = kd.get_girl_group(gid)
        return render_template('13.gg_update.html', group=group)
    else:
        name = request.form['name']
        debut = request.form['debut']
        hid = request.form['hid']
        kd.update_girl_group((name, debut, hid, gid))
        return redirect('/gg/list')
    
@app.route('/gg/delete/<gid>')
def gg_delete(gid):
    kd.delete_girl_group(gid)
    return redirect('/gg/list')

if __name__ == '__main__':
    app.run(debug=True)