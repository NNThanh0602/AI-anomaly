import pandas as pd
import ipaddress

def preprocess_data(file_path, output_path):
    df = pd.read_csv(file_path)
    df['@timestamp'] = pd.to_datetime(df['@timestamp'], errors='coerce')
    df['hour'] = df['@timestamp'].dt.hour
    df['day'] = df['@timestamp'].dt.day
    df['weekday'] = df['@timestamp'].dt.weekday

    def ip_to_int(ip):
        try:
            return int(ipaddress.IPv4Address(ip))
        except:
            return 0
    
    df['host.ip'] = df['host.ip'].apply(ip_to_int)
    selected_columns = ['host.ip', 'hour', 'day', 'weekday', 'event.code', 'event.duration', 'host.cpu.usage']
    df = df[selected_columns].fillna(0)
    df.to_csv(output_path, index=False)

def run(input_file, output_file):
    preprocess_data(input_file, output_file)