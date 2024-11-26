from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(_name_)

# Load the model
model = tf.keras.models.load_model('models/trained_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('data')
    data = np.array(data)
    predictions = model.predict(data).tolist()
    return jsonify({'predictions': predictions})

if __name___ == "__main__":
    app.run(host='0.0.0.0', port=5000)