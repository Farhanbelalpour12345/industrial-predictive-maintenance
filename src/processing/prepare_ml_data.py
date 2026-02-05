import pandas as pd

def create_rul(df):
    max_cycles = df.groupby("unit")["cycle"].max()
    df = df.merge(max_cycles.rename("max_cycle"), on="unit")
    df["RUL"] = df["max_cycle"] - df["cycle"]
    df.drop(columns=["max_cycle"], inplace=True)
    return df
