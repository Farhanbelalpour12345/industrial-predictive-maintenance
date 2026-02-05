import os
import pandas as pd

from src.ingestion.load_data import load_data
from src.processing.clean_data import clean_data
from src.features.build_features import add_rolling_features
from src.processing.prepare_ml_data import create_rul

OUTPUT_PATH = os.path.join("data", "processed", "processed_data.csv")

def main():
    print("🔹 Loading data...")
    df = load_data()
    print("Shape after loading:", df.shape)

    print("🔹 Cleaning data...")
    df = clean_data(df)
    print("Shape after cleaning:", df.shape)

    print("🔹 Building rolling features...")
    df = add_rolling_features(df)
    print("Shape after feature engineering:", df.shape)

    print("🔹 Creating RUL target...")
    df = create_rul(df)
    print("Shape after adding RUL:", df.shape)

    print("🔹 Saving processed dataset...")
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print("✅ Pipeline finished. File saved at:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
