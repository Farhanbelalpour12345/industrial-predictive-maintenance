import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import os

DATA_PATH = os.path.join("data", "processed", "processed_data.csv")
OUTPUT_PATH = os.path.join("data", "processed", "rul_predictions.csv")

def load_processed_data():
    return pd.read_csv(DATA_PATH)

def train_rul_model(df: pd.DataFrame):
    feature_cols = [c for c in df.columns if "sensor" in c or "rolling" in c]

    X = df[feature_cols]
    y = df["RUL"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    results = X_test.copy()
    results["true_RUL"] = y_test.values
    results["predicted_RUL"] = preds

    os.makedirs("data/processed", exist_ok=True)
    results.to_csv(OUTPUT_PATH, index=False)

    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"Predictions saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    df = load_processed_data()
    train_rul_model(df)
