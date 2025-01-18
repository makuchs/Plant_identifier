import os
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

AZURE_API_URL = "https://plant-identifier-chd4eeb5deeqa8ec.polandcentral-01.azurewebsites.net/predict"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        response = requests.post(
            AZURE_API_URL,
            files={"file": (file.filename, file.stream, file.content_type)},
            timeout= 30 
        )

        if response.status_code == 200:
            result = response.json()
        else:
            result = {'error': 'Azure API error', 'status_code': response.status_code}

    except requests.exceptions.Timeout:
        result = {'error': 'Request to Azure API timed out'}
    except Exception as e:
        result = {'error': str(e)}

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)