import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
import joblib

# 1. 데이터 불러오기
print("[INFO] Loading dataset...")
df = pd.read_csv("creditcard.csv")

# 2. 특성과 타겟 분리
X = df.drop("Class", axis=1)
y = df["Class"]

# 3. 학습/테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# 4. 모델 학습
print("[INFO] Training LGBMClassifier...")
model = LGBMClassifier()
model.fit(X_train, y_train)

# 5. 모델 저장
print("[INFO] Saving model to lgbm_model2.pkl...")
joblib.dump(model, "lgbm_model2.pkl")

print("[INFO] Done. Model saved.")