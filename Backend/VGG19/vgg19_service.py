from flask import Flask, request, jsonify
import numpy as np
import librosa
import base64
import io
from tensorflow.keras.models import load_model
import joblib

app = Flask(__name__)

# Charger le modèle VGG19
vgg19_model = load_model('vgg19_model.h5')
label_encoder = joblib.load('label_encoder.pkl')

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    spectrogram = librosa.power_to_db(spectrogram, ref=np.max)
    spectrogram = spectrogram.reshape(1, 128, 128, 1)
    return spectrogram

@app.route('/vgg19_service', methods=['POST'])
def vgg19_service():
    data = request.get_json()
    wav_base64 = data['wav_music']
    wav_data = base64.b64decode(wav_base64)
    y, sr = librosa.load(io.BytesIO(wav_data), sr=None)
    spectrogram = extract_features(y)
    genre = vgg19_model.predict(spectrogram)
    genre = np.argmax(genre, axis=1)
    genre = label_encoder.inverse_transform(genre)
    return jsonify({'genre': genre[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
