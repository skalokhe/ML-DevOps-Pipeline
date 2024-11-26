import tensorflow as tf
from flask import Flask, request, jsonify, render_template
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for browser access

def create_model():
    inputs = tf.keras.Input(shape=(4,))
    x = tf.keras.layers.Dense(64, activation='relu')(inputs)
    x = tf.keras.layers.Dense(32, activation='relu')(x)
    outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)
    model = tf.keras.Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

model = create_model()

@app.route('/')
def home():
    return jsonify({
        'status': 'online',
        'endpoints': {
            'health': '/health [GET]',
            'predict': '/predict [POST]'
        }
    })

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return jsonify({
            'message': 'Please use POST method with JSON data',
            'example': {
                'data': [[0.5, 0.8, 0.3, 0.7]]
            }
        })
    
    try:
        input_data = request.get_json()
        features = np.array(input_data['data'], dtype=np.float32)
        predictions = model.predict(features)
        return jsonify({
            'status': 'success',
            'predictions': predictions.tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': 'Bad Request', 'message': str(e)}), 400

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method Not Allowed', 'message': str(e)}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
