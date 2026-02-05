import streamlit as st
import pandas as pd
import os

DATA_PATH = os.path.join("data", "processed", "rul_predictions.csv")

st.set_page_config(page_title="Predictive Maintenance Dashboard", layout="wide")

st.title("🛠 Predictive Maintenance – RUL Monitoring")

df = pd.read_csv(DATA_PATH)

st.subheader("📊 RUL Prediction Overview")
st.dataframe(df.head(50))

st.subheader("📉 True vs Predicted RUL")
st.line_chart(df[["true_RUL", "predicted_RUL"]])

st.subheader("⚠️ Critical Machines")
critical = df[df["predicted_RUL"] < 30]
st.write(f"Machines at risk: {len(critical)}")
st.dataframe(critical.head(20))
