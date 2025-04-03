import pandas as pd
import requests
import time
from collections import Counter

# 데이터 불러오기
df = pd.read_csv("creditcard.csv")
X = df.drop("Class", axis=1)

# 서버 URL
url = "http://127.0.0.1:9999/predict"

# 카운터 초기화
result_counter = Counter()

# 실시간처럼 보내기 (예: 처음 100건)
for i in range(100):
    sample = X.iloc[i].to_dict()

    try:
        res = requests.post(url, json=[sample])  # 리스트로 감싸기
        result = res.json()['prediction'][0]
        result_counter[result] += 1

        print(f"[{i+1:03}] 예측 결과: {result} → 현재까지 (정상: {result_counter[0]}, 사기: {result_counter[1]})")

        time.sleep(0.2)  # 실시간처럼 약간 지연 주기 (선택)

    except Exception as e:
        print(f"[ERROR] {e}")
        continue

# 최종 결과 출력
print("\n=== 예측 결과 요약 ===")
print(f"정상 거래 (0): {result_counter[0]}건")
print(f"사기 거래 (1): {result_counter[1]}건")