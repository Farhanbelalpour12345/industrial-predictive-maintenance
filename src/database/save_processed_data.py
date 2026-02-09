import pandas as pd
from src.database.db_connection import get_engine

TABLE_NAME = "processed_sensor_data"

def save_processed_data():
    df = pd.read_csv("data/processed/processed_data.csv")
    engine = get_engine()

    df.to_sql(
        TABLE_NAME,
        engine,
        if_exists="replace",
        index=False
    )

    print("Processed data saved to PostgreSQL")

if __name__ == "__main__":
    save_processed_data()
