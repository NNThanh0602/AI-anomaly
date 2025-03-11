import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
import joblib

def train_model(data_path, model_path):
    df = pd.read_csv(data_path)

    # Xử lý dữ liệu lỗi
    df.replace('-', np.nan, inplace=True)  # Chuyển '-' thành NaN
    df.replace({",": ""}, regex=True)  # Xóa dấu phẩy trong số lớn
    df = df.apply(pd.to_numeric, errors='coerce')  # Chuyển về số
    df.fillna(0, inplace=True)  # Điền lại NaN nếu có

    # Chuẩn hóa dữ liệu
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    # Huấn luyện mô hình Isolation Forest
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(df_scaled)

    # Lưu mô hình và bộ chuẩn hóa
    joblib.dump(model, model_path)
    joblib.dump(scaler, "scaler.pkl")

def run(data_path, model_path):
    train_model(data_path, model_path)