import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import os

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    features = data[["feature1", "feature2", "feature3", "feature4"]].values
    labels = data["label"].values
    return features, labels

def train_and_save_model(data, labels, save_path):
    model = Sequential([
        Dense(64, activation='relu', input_shape=(data.shape[1],)),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(data, labels, epochs=10, batch_size=128)
    model.save(save_path)
    print(f"Model saved to {save_path}")

if __name__ == "__main__":
    dataset_path = "data/large_dataset.csv"
    features, labels = preprocess_data(dataset_path)
    save_path = os.path.join('models', 'trained_model.h5')
    train_and_save_model(features, labels, save_path)
