from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/svm_service', methods=['POST'])
def svm_service():
    data = request.get_json()
    response = requests.post('http://svm_service:5000/svm_service', json=data)
    return jsonify(response.json())

@app.route('/vgg19_service', methods=['POST'])
def vgg19_service():
    data = request.get_json()
    response = requests.post('http://vgg19_service:5001/vgg19_service', json=data)
    return jsonify(response.json())
@app.route("/")
def home():
    return "Hello, Flask!"
if __name__ == "__main__":
    app.run(debug=True)
