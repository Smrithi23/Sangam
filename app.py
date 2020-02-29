import flask
from flask import request, jsonify
from json import dumps
from flask import *
import yolo
import yolo_utils
import os
from yolo_photo import photo_labels

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        if "file" not in request.files:
            return flask.Response('No file part')
        else:
            file = request.files["file"]
            if file and allowed_file(file.filename):
                labels=[]
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                path='./uploads/image.png'
                labels=photo_labels(path)
                print(labels)
                i=0
                for label in labels:
                    labels[i]=label.split(':')[0]
                    i=i+1
                return flask.Response(dumps(labels))  

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)