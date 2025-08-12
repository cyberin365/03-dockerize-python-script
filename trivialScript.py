# what this code does doesn't matter
# i just want it to have dependencies
 

from sklearn.datasets import load_iris
import pandas as pd

def main():
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

    print(iris_df)

if __name__ == "__main__":
    main()

