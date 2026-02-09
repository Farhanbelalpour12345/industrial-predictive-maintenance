import pandas as pd
from src.database.db_connection import get_engine

TABLE_NAME = "rul_predictions"

def save_predictions():
    df = pd.read_csv("data/processed/rul_predictions.csv")
    engine = get_engine()

    df.to_sql(
        TABLE_NAME,
        engine,
        if_exists="replace",
        index=False
    )

    print("Predictions saved to PostgreSQL")

if __name__ == "__main__":
    save_predictions()
