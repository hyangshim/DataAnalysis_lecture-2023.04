from flask import Flask, render_template, request,redirect,session,flash
import melon as melon

app =Flask(__name__)
@app.route('/melon')
def melon():
    melon_list = melon.melon() 
    return render_template('melon.html',melon_list=melon_list)


if __name__ == '__main__':
    app.run(debug=True)