def add_rolling_features(df):
    df = df.copy()
    sensor_cols = [c for c in df.columns if "sensor" in c]

    for col in sensor_cols:
        df[f"{col}_rolling_mean"] = df.groupby("unit")[col].rolling(5).mean().reset_index(0, drop=True)
        df[f"{col}_rolling_std"] = df.groupby("unit")[col].rolling(5).std().reset_index(0, drop=True)

    df.fillna(0, inplace=True)
    return df
