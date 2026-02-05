from sklearn.ensemble import IsolationForest

def train_anomaly_model(df):
    feature_cols = [c for c in df.columns if "sensor" in c]
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(df[feature_cols])
    df["anomaly_score"] = model.decision_function(df[feature_cols])
    df["anomaly"] = model.predict(df[feature_cols])
    return model, df
