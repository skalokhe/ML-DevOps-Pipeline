import pytest
import numpy as np
from src.training.train_model import train_and_save_model
from src.deployment.serve_model import app

def test_model_training():
    data = np.random.rand(100, 10)
    labels = np.random.randint(2, size=(100, 1))
    train_and_save_model(data, labels, 'test_model.h5')
    assert True  # Add specific checks, e.g., file existence

def test_model_prediction():
    client = app.test_client()
    response = client.post('/predict', json={"data": [[0.5, 1.2, 3.1, 4.6]]})
    assert response.status_code == 200
    assert 'predictions' in response.get_json()
