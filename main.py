import preprocess
import train_model
import detect_anomaly

def main():
    print("B?t ??u x? l� log...")
    preprocess.run("logs.csv", "processed_logs.csv")
    print("Hu?n luy?n m� h�nh...")
    train_model.run("processed_logs.csv", "model.pkl")
    print("Ph�t hi?n b?t th??ng...")
    detect_anomaly.run("processed_logs.csv", "model.pkl")
    print("Ho�n th�nh! K?t qu? l?u trong anomaly_detected.csv")

if __name__ == "__main__":
    main()
