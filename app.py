import streamlit as st

# 1. 기존 app.db.database.py에 있던 클래스를 내장시킵니다.
class Database:
    def __init__(self):
        # 데이터베이스 초기화 로직 (필요시 작성)
        pass
        
    def save_iris(self, sl, sw, pl, pw, result):
        # 데이터베이스 저장 로직 (필요시 작성)
        pass
        
    def get_result_stats(self):
        # Streamlit 차트가 정상 작동하도록 임시/기본 통계 데이터를 리턴합니다.
        # 나중에 실제 DB 데이터로 연결하시면 됩니다.
        return [("Setosa", 12), ("Versicolor", 18), ("Virginica", 9)]

# 2. 기존 app.ml.predictor.py에 있던 함수를 내장시킵니다.
def predict_iris(features):
    # 머신러닝 예측 모델이 들어갈 자리입니다.
    # 우선 화면 테스트를 위해 기본값으로 "Setosa"를 반환하게 만듭니다.
    return "Setosa"


# 3. Streamlit 웹 인터페이스 및 실행 로직
db = Database()

st.title("🌸 Iris Classifier")

sl = st.number_input("Sepal Length", 5.0)
sw = st.number_input("Sepal Width", 3.0)
pl = st.number_input("Petal Length", 1.5)
pw = st.number_input("Petal Width", 0.2)

if st.button("Predict"):
    result = predict_iris([sl, sw, pl, pw])
    db.save_iris(sl, sw, pl, pw, result)
    st.success(result)
    
    

stats = db.get_result_stats()
st.bar_chart(dict(stats))