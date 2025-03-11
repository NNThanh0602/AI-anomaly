import preprocess
import train_model
import detect_anomaly

def main():
    print("B?t ??u x? lý log...")
    preprocess.run("logs.csv", "processed_logs.csv")
    print("Hu?n luy?n mô hình...")
    train_model.run("processed_logs.csv", "model.pkl")
    print("Phát hi?n b?t th??ng...")
    detect_anomaly.run("processed_logs.csv", "model.pkl")
    print("Hoàn thành! K?t qu? l?u trong anomaly_detected.csv")

if __name__ == "__main__":
    main()
