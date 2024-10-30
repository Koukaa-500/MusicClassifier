from flask import Flask, request, jsonify
import joblib
import numpy as np
import librosa
import base64
import io

app = Flask(__name__)

# Charger le modèle SVM
svm_model = joblib.load('svm_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc.T, axis=0)
    return mfcc_mean

@app.route('/svm_service', methods=['POST'])
def svm_service():
    data = request.get_json()
    wav_base64 = data['wav_music']
    wav_data = base64.b64decode(wav_base64)
    y, sr = librosa.load(io.BytesIO(wav_data), sr=None)
    features = extract_features(y)
    genre = svm_model.predict([features])
    genre = label_encoder.inverse_transform(genre)
    return jsonify({'genre': genre[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
