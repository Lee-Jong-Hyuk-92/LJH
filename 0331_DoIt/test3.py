import requests
import pandas as pd
import json
import time

data = pd.read_csv('X_train_over.csv')

# JSON 형태로 변환
records = data.to_dict(orient='records')

url = 'http://127.0.0.1:9999/predict'

batch_size = 2000
total = len(records)

for start in range(0, total, batch_size):
    end = min(start + batch_size, total)
    batch = records[start:end]

    try:
        response = requests.post(url, json=batch)
        if response.status_code == 200:
            result = response.json()
            print(f"[{start}-{end}] Prediction:", result['prediction'])

        else:
            print(f"[{start}-{end}] Error:", response.status_code, response.text)
            
    except Exception as e:
        print(f"[{start}-{end}] Exception occurred:", str(e))

    time.sleep(2)  # 전송시간 간격
