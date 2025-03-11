import pandas as pd
import joblib

def detect_anomalies(data_path, model_path):
    df = pd.read_csv(data_path)
    model = joblib.load(model_path)
    scaler = joblib.load("scaler.pkl")
    df_scaled = scaler.transform(df)
    df['anomaly'] = model.predict(df_scaled)
    df['anomaly'] = df['anomaly'].apply(lambda x: "Anomaly" if x == -1 else "Normal")
    df.to_csv("anomaly_detected.csv", index=False)

def run(data_path, model_path):
    detect_anomalies(data_path, model_path)
