import requests
import pandas as pd
import json
import time

data = pd.read_csv('creditcard.csv')

# JSON 형태로 변환
records = data.to_dict(orient='records')

url = 'http://127.0.0.1:9999/predict'
stats_url = 'http://127.0.0.1:9999/stats'

batch_size = 10000
total = len(records)
all_predictions = []

for start in range(0, total, batch_size):
    end = min(start + batch_size, total)
    batch = records[start:end]

    try:
        response = requests.post(url, json=batch)
        
        if response.status_code == 200:
            result = response.json()
            predictions = result['prediction']
            all_predictions.extend(predictions)
            print(f"[{start}-{end}] Prediction OK")
        else:
            print(f"[{start}-{end}] Error:", response.status_code, response.text)
    except Exception as e:
        print(f"[{start}-{end}] Exception occurred:", str(e))

    time.sleep(0.1)  # 보내는 시간 간격격

# 예측 결과를 원본 데이터에 붙이기
data['prediction'] = all_predictions

# 저장
data.to_csv('X_train_over.csv', index=False)
print("예측 결과가 'X_train_over.csv'에 저장되었습니다.")

# 서버에 stats 요청
try:
    stats_response = requests.get(stats_url)
    if stats_response.status_code == 200:
        stats = stats_response.json()
        print("예측 통계:")
        for label, count in stats.items():
            label_str = "사기" if label == "1" else "정상"
            print(f" - {label_str} ({label}): {count}건")
    else:
        print("통계 요청 실패:", stats_response.status_code, stats_response.text)
except Exception as e:
    print("통계 요청 중 예외 발생:", str(e))