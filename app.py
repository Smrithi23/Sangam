import pyrebase
import flask
from flask import request
from flask import *
import yolo
import yolo_utils
config = {
    "apiKey": "AIzaSyBWOx1eY5_3uVqNX4lZzzGJSEslxbT1dcU",
    "authDomain": "sangam-781b3.firebaseapp.com",
    "databaseURL": "https://sangam-781b3.firebaseio.com",
    "projectId": "sangam-781b3",
    "storageBucket": "sangam-781b3.appspot.com",
    "messagingSenderId": "462352486294",
    "appId": "1:462352486294:web:f47fc53110552f6350d7b7"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

app = Flask(__name__)

@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        if "file" not in request.files:
            return flask.Response('No file part')
        else:
            file = request.files["file"]
            storage.child(file.filename).put("image.jpg")
            return flask.Response("Uploaded Successfully")

@app.route('/', methods = ['GET'])
def send():
    if request.method == 'GET':
        return yolo_utils.infer_image()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)