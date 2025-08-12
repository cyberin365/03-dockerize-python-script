# what this code does doesn't matter
# i just want it to have dependencies
 

from sklearn.datasets import load_iris
import pandas as pd
import random

csv_path = "iris.csv"

# Read the CSV
iris_df = pd.read_csv(csv_path)

# Pick a random number between 1 and the number of available rows (max 10)
max_rows = min(len(iris_df), 10)
n_rows = random.randint(1, max_rows)

# Filter down to n_rows
filtered_df = iris_df.sample(n=n_rows, random_state=random.randint(0, 10000))

# Overwrite the CSV with the filtered DataFrame
filtered_df.to_csv(csv_path, index=False)

print(f"Wrote {n_rows} rows to {csv_path}")

def main():
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

    print(iris_df)

if __name__ == "__main__":
    main()

