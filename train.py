from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# 데이터 로드
iris = load_iris()

X = iris.data
y = iris.target

# 모델 생성
model = RandomForestClassifier()

# 학습
model.fit(X, y)

# 저장
joblib.dump(model, "iris_model.pkl")

print("모델 저장 완료")