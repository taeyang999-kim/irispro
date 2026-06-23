import streamlit as st
import random

# 1. DB (발표용 Mock DB)
class Database:
    def __init__(self):
        self.data = []

    def save_iris(self, sl, sw, pl, pw, result):
        self.data.append({
            "sl": sl,
            "sw": sw,
            "pl": pl,
            "pw": pw,
            "result": result
        })

    def get_result_stats(self):
        stats = {"Setosa": 0, "Versicolor": 0, "Virginica": 0}
        for d in self.data:
            stats[d["result"]] += 1
        return stats


# 2. ML 모델 (발표용 간단 버전)
def predict_iris(features):
    sl, sw, pl, pw = features

    # 아주 단순한 규칙 기반 (발표용 설명 가능)
    if pl < 2:
        return "Setosa"
    elif pl < 5:
        return "Versicolor"
    else:
        return "Virginica"


# 3. 앱 초기화
db = Database()

st.set_page_config(page_title="Iris ML Service", page_icon="🌸", layout="centered")

st.title("🌸 Iris Flower Classification Service")
st.caption("Machine Learning 기반 꽃 종류 예측 웹 애플리케이션")

st.markdown("---")


# 4. 입력 UI
st.subheader("📥 꽃 정보 입력")

col1, col2 = st.columns(2)

with col1:
    sl = st.number_input("Sepal Length", value=5.0)
    sw = st.number_input("Sepal Width", value=3.0)

with col2:
    pl = st.number_input("Petal Length", value=1.5)
    pw = st.number_input("Petal Width", value=0.2)

st.markdown("---")

# 5. 예측
if st.button("🌸 Predict Species"):

    result = predict_iris([sl, sw, pl, pw])
    db.save_iris(sl, sw, pl, pw, result)

    st.success(f"🌸 Prediction Result: **{result}**")

    st.info(
        f"""
        📌 입력값 요약  
        - Sepal Length: {sl}  
        - Sepal Width: {sw}  
        - Petal Length: {pl}  
        - Petal Width: {pw}
        """
    )


st.markdown("---")


# 6. 통계 그래프
st.subheader("📊 Prediction Statistics")

stats = db.get_result_stats()

if sum(stats.values()) > 0:
    st.bar_chart(stats)
else:
    st.warning("아직 예측 데이터가 없습니다.")


# 7. 설명 (발표용 포인트)
with st.expander("📘 프로젝트 설명 보기"):
    st.write("""
    이 프로젝트는 머신러닝 기반 Iris 꽃 분류 서비스입니다.

    - 사용자가 꽃의 4가지 특징을 입력하면
    - 머신러닝 모델이 꽃의 종류를 예측합니다.
    - 예측 결과는 저장되고 통계로 시각화됩니다.

    👉 Streamlit을 이용해 웹 서비스 형태로 구현했습니다.
    """)