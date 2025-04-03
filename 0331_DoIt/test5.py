import requests
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

data = pd.read_csv('creditcard.csv')
records = data.to_dict(orient='records')
url = 'http://127.0.0.1:9999/predict'

batch_size = 10000
total = len(records)

def send_request(start, end):
    batch = records[start:end]
    try:
        response = requests.post(url, json=batch)
        if response.status_code == 200:
            predictions = response.json()['prediction']
            print(f"[{start}-{end}] ✅ Prediction OK")
            return (start, end, predictions)
        else:
            print(f"[{start}-{end}] ❌ Error:", response.status_code)
    except Exception as e:
        print(f"[{start}-{end}] ❌ Exception:", str(e))
    return (start, end, [])

# 병렬 요청
all_predictions = [None] * total
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [
        executor.submit(send_request, start, min(start + batch_size, total))
        for start in range(0, total, batch_size)
    ]
    for future in as_completed(futures):
        start, end, preds = future.result()
        all_predictions[start:end] = preds

# 저장
data['prediction'] = all_predictions
data.to_csv('X_train_over.csv', index=False)
print("✅ 예측 결과 저장 완료")