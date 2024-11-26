import pandas as pd
import time
import random

def simulate_data_stream(file_path):
    data = pd.read_csv(file_path)
    for _, row in data.iterrows():
        yield row.to_dict()

if __name__ == "__main__":
    stream = simulate_data_stream("data/large_dataset.csv")
    for record in stream:
        print(f"Processing: {record}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate delay
