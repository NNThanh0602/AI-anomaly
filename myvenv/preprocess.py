import pandas as pd
import ipaddress

def preprocess_data(file_path, output_path):
    df = pd.read_csv(file_path)

    # Chuyển đổi @timestamp thành datetime và trích xuất thông tin thời gian
    df["@timestamp"] = pd.to_datetime(df["@timestamp"], format="%b %d, %Y @ %H:%M:%S.%f", errors="coerce")
    df["hour"] = df["@timestamp"].dt.hour
    df["day"] = df["@timestamp"].dt.day
    df["weekday"] = df["@timestamp"].dt.weekday

    # Xử lý host.ip: Chuyển IPv4 thành số nguyên
    def convert_ip(ip):
        try:
            ip_list = ip.split(",")  # Nếu có nhiều IP, lấy IPv4
            for i in ip_list:
                if "." in i:  # Chọn IP dạng IPv4
                    return int(ipaddress.IPv4Address(i.strip()))
        except:
            return 0
        return 0

    df["winlog.event_data.SourceAddress"] = df["winlog.event_data.SourceAddress"].apply(convert_ip)
    df["winlog.event_data.DestAddress"] = df["winlog.event_data.DestAddress"].apply(convert_ip)


    # Xóa dấu phẩy trong các số lớn
    df.replace({",": ""}, regex=True, inplace=True)

    # Chuyển các cột quan trọng thành số
    columns_to_convert = ["event.code", "event.duration", "host.cpu.usage"]
    for col in columns_to_convert:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Xử lý NaN theo từng kiểu dữ liệu
    df.fillna({"@timestamp": pd.NaT, "winlog.event_data.SourceAddress": 0,"winlog.event_data.DestAddress": 0, "event.code": 0, "event.duration": 0, "host.cpu.usage": 0}, inplace=True)

    # Chọn cột theo định dạng CSV chuẩn
    selected_columns = ["winlog.event_data.SourceAddress", "winlog.event_data.DestAddress", "hour", "day", "weekday", "event.code", "event.duration", "host.cpu.usage"]
    df = df[selected_columns].copy()

    # Ghi ra file CSV
    try:
        df.to_csv(output_path, index=False)
        print(f"Xuất dữ liệu thành công: {output_path}")
    except PermissionError:
        print(f"LỖI: Không thể ghi vào {output_path}. Đảm bảo tệp không bị mở và bạn có quyền ghi.")

def run(input_file, output_file):
    preprocess_data(input_file, output_file)
