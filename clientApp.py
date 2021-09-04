from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from utils.utils import decodeImage
from predict import ship
from wsgiref import simple_server

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = ship(self.filename)



@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')
    


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image,clApp.filename)
    result = clApp.classifier.shipdetection()
    return jsonify(result)


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    #port = int(os.getenv("PORT"))
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host,port=5000, app=app)
    httpd.serve_forever()
