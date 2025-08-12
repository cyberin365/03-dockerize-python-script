# what this code does doesn't matter
# i just want it to have dependencies
 

from sklearn.datasets import load_iris
import os
import pandas as pd
import random

csv_path = "iris.csv"

# Read environment variables
max_rows_env = int(os.environ.get("MAX_ROWS", 10))
random_seed = int(os.environ.get("RANDOM_SEED", random.randint(0, 10000)))

# Load the full Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Determine how many rows to sample
max_rows = min(len(iris_df), max_rows_env)
n_rows = random.randint(1, max_rows)

# Sample and overwrite the CSV
filtered_df = iris_df.sample(n=n_rows, random_state=random_seed)
filtered_df.to_csv(csv_path, index=False)

print(f"Wrote {n_rows} rows to {csv_path} with seed {random_seed}")

def main():
    print(filtered_df)

if __name__ == "__main__":
    main()

