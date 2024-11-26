from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def metrics():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    return jsonify({
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "status": "Healthy" if cpu_usage < 80 else "Degraded"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
