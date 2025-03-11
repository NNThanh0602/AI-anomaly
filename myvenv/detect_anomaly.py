import pandas as pd
import numpy as np
import joblib

def detect_anomalies(data_path, model_path):
    df = pd.read_csv(data_path)

    # Xử lý dữ liệu lỗi
    df.replace('-', np.nan, inplace=True)  # Chuyển '-' thành NaN
    df.replace({",": ""}, regex=True)  # Xóa dấu phẩy trong số lớn
    df = df.apply(pd.to_numeric, errors='coerce')  # Chuyển về số
    df.fillna(0, inplace=True)  # Điền lại NaN nếu có

    # Tải mô hình và scaler
    model = joblib.load(model_path)
    scaler = joblib.load("scaler.pkl")

    # Chuẩn hóa dữ liệu
    df_scaled = scaler.transform(df)

    # Phát hiện bất thường
    df['anomaly'] = model.predict(df_scaled)
    df['anomaly'] = df['anomaly'].apply(lambda x: "Anomaly" if x == -1 else "Normal")

    

    # Lưu kết quả
    df.to_csv("anomaly_detected.csv", index=False)

def run(data_path, model_path):
    detect_anomalies(data_path, model_path)