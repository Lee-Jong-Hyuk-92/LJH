import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
import joblib

# 데이터 불러오기
df = pd.read_csv("creditcard.csv")

# 간단한 전처리 (Class가 타겟)
X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# 모델 학습
model = LGBMClassifier()
model.fit(X_train, y_train)

# 저장
joblib.dump(model, "lgbm_model.pkl")