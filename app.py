from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('fault_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    current = float(data.get('current', 0))
    voltage = float(data.get('voltage', 0))
    frequency = float(data.get('frequency', 50))
    power_factor = float(data.get('power_factor', 1.0))

    features = np.array([[current, voltage, frequency, power_factor]])

    probability = model.predict_proba(features)[0]
    fault_confidence = probability[1]

    return jsonify({
        'confidence': float(fault_confidence)
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ML service running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
