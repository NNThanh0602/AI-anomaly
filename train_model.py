import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

def train_model(data_path, model_path):
    df = pd.read_csv(data_path)
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(df_scaled)
    joblib.dump(model, model_path)
    joblib.dump(scaler, "scaler.pkl")

def run(data_path, model_path):
    train_model(data_path, model_path)