import pandas as pd
import numpy as np

# Generate a dataset with 10,000 rows and 4 features
n_rows = 10000
data = {
    "feature1": np.random.rand(n_rows),
    "feature2": np.random.rand(n_rows),
    "feature3": np.random.rand(n_rows),
    "feature4": np.random.rand(n_rows),
    "label": np.random.randint(0, 2, size=n_rows),
}

df = pd.DataFrame(data)
df.to_csv("data/large_dataset.csv", index=False)
print("Dataset with 10,000 rows has been generated.")
