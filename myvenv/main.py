import preprocess
import train_model
import detect_anomaly

def main():
    print("Bat xu ly log...")
    preprocess.run(
        r"C:\Users\Administrator.WINSV-ADMIN\Downloads\logs.csv", 
        r"C:\Users\Administrator.WINSV-ADMIN\Desktop\check\processed_logs.csv"
    )
    print("Huan luyen mo hinh...")
    train_model.run(
        r"C:\Users\Administrator.WINSV-ADMIN\Desktop\check\processed_logs.csv", 
        "model.pkl"
    )
    print("Phat hien bat thuong...")
    detect_anomaly.run(
        r"C:\Users\Administrator.WINSV-ADMIN\Desktop\check\processed_logs.csv", 
        "model.pkl"
    )
    print("Hoan thanh! Ket qua lu trong anomaly_detected.csv")

if __name__ == "__main__":
    main()
