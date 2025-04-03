import pandas as pd
import requests

# 데이터 로드
df = pd.read_csv("creditcard.csv")

# 타겟 변수 제거
X = df.drop("Class", axis=1)

# 아무 행이나 하나 선택 (예: 첫 번째 행)
sample = X.iloc[0].to_dict()

# 서버 URL
url = "http://127.0.0.1:9999/predict"

# POST 요청
res = requests.post(url, json=[sample])

# 결과 출력
print(res.json())