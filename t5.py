from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session,
    url_for, jsonify, Response
)
import requests
import time

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
    parameter = url.replace("http://127.0.0.1:5000", "")
    parameter = parameter.replace(path, "")

    if request.method == 'HEAD':
        r = requests.head('http://model3d.4dage.com/model/' + str(uuid) + ".4dage" + parameter)
    elif request.method == 'GET':
        r = requests.get('http://model3d.4dage.com/model/' + str(uuid) + ".4dage" + parameter)

    return Response(r.content, content_type="application/octet-stream")


@app.route('/<uuid>/thumbnail.jpg')
def thumbnail_jpg(uuid):
    url = request.url
    path = request.path
    parameter = url.replace("http://127.0.0.1:5000", "")
    parameter = parameter.replace(path, "")
    r = requests.get('http://model3d.4dage.com/model/' + str(uuid) + "/thumbnail.jpg" + parameter)
    resp = Response(r, mimetype="image/jpeg")
    return resp


if __name__ == '__main__':
    app.run()
