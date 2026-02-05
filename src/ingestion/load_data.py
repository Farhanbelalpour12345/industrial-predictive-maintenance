import pandas as pd
import os

DATA_PATH = os.path.join("data", "raw", "train_FD001.txt")

# 26 ستون واقعی دیتاست
COLS = (
    ["unit", "cycle"] +
    [f"op_setting_{i}" for i in range(1, 4)] +
    [f"sensor_{i}" for i in range(1, 22)]
)

def load_data():
    df = pd.read_csv(DATA_PATH, sep="\s+", header=None)
    df.columns = COLS
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
    print("\nShape:", df.shape)
