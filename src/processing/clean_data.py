import pandas as pd

def clean_data(df):
    df = df.copy()

    # حذف ستون‌های با واریانس خیلی کم
    low_var_cols = [col for col in df.columns if df[col].std() < 0.01]
    df.drop(columns=low_var_cols, inplace=True)

    # نرمال‌سازی ساده
    sensor_cols = [c for c in df.columns if "sensor" in c]
    df[sensor_cols] = (df[sensor_cols] - df[sensor_cols].mean()) / df[sensor_cols].std()

    return df
