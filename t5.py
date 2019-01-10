from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session,
    url_for, jsonify, Response
)
import requests
import time
import shelve

app = Flask(__name__, static_url_path='')
app.debug=True


@app.route('/')
def model():
    path = request.path
    r = requests.get('http://model3d.4dage.com/model' + path)
    return r.text


@app.route('/showModel.html')
def showModel_html():
    return render_template('showModel.html')


@app.route('/<uuid>.4dage')
def uuid_name(uuid):
    url = request.url
    path = request.path
    parameter = url.replace("https://3d.xixilog.com", "")
    parameter = parameter.replace(path, "")

    if request.method == 'HEAD':
        try:
            with shelve.open('shelve.db') as db:
                name = str(uuid) + "_4dage_HEAD"
                r = db[name]
        except:
            r = requests.head('http://model3d.4dage.com/model/' + str(uuid) + ".4dage" + parameter)
            with shelve.open('shelve.db') as db:
                name = str(uuid) + "_4dage_HEAD"
                db[name] = r

    if request.method == 'GET':
        try:
            with shelve.open('shelve.db') as db:
                name = str(uuid) + "_4dage_GET"
                r = db[name]
                with open(str(uuid) + '.4dage', 'wb') as file:
                    file.write(r.content)
        except:
            r = requests.get('http://model3d.4dage.com/model/' + str(uuid) + ".4dage" + parameter)
            with shelve.open('shelve.db') as db:
                name = str(uuid) + "_4dage_GET"
                db[name] = r

    return Response(r.content, content_type="application/octet-stream")


@app.route('/<uuid>/thumbnail.jpg')
def thumbnail_jpg(uuid):
    url = request.url
    path = request.path
    parameter = url.replace("https://3d.xixilog.com", "")
    parameter = parameter.replace(path, "")
    db = shelve.open('shelve.db')

    try:
        name = str(uuid) + "_thumbnail"
        r = db[name]
        with open('thumbnail.jpg', 'wb') as file:
            file.write(r.content)
    except:
        r = requests.get('http://model3d.4dage.com/model/' + str(uuid) + "/thumbnail.jpg" + parameter)
        name = str(uuid) + "_thumbnail"
        db[name] = r

    db.close()
    resp = Response(r, mimetype="image/jpeg")
    return resp


app.run()
