import streamlit as st
import pandas as pd

# 1. DB (발표용 Mock DB)
class Database:
    def __init__(self):
        self.data = []

    def save_iris(self, sl, sw, pl, pw, result):
        self.data.append({
            "Sepal Length": sl,
            "Sepal Width": sw,
            "Petal Length": pl,
            "Petal Width": pw,
            "Result": result
        })

    def get_result_stats(self):
        stats = {"Setosa": 0, "Versicolor": 0, "Virginica": 0}
        for d in self.data:
            stats[d["Result"]] += 1
        return stats


# 2. ML 모델 (발표용 규칙 기반)
def predict_iris(features):
    sl, sw, pl, pw = features

    if pl < 2:
        return "Setosa"
    elif pl < 5:
        return "Versicolor"
    else:
        return "Virginica"


# 3. 앱 초기화
db = Database()

st.set_page_config(
    page_title="Iris ML Service",
    page_icon="🌸",
    layout="centered"
)

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

    st.metric(label="Predicted Class", value=result)

    st.info(
        f"""
        📌 입력값 요약  
        - 꽃받침 길이(Sepal Length): {sl}  
        - 꽃받침 너비(Sepal Width): {sw}  
        - 꽃잎 길이(Petal Length): {pl}  
        - 꽃잎 너비(Petal Width): {pw}
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


# 7. 최근 기록 (🔥 추가 기능)
st.subheader("📋 Recent Predictions")

if len(db.data) > 0:
    df = pd.DataFrame(db.data)
    st.dataframe(df.tail(10))
else:
    st.info("아직 저장된 데이터가 없습니다.")


# 8. 초기화 버튼 (🔥 추가 기능)
if st.button("🧹 Reset All Data"):
    db.data.clear()
    st.success("모든 데이터가 초기화되었습니다.")
    st.rerun()


# 9. 설명 (발표용)
with st.expander("📘 프로젝트 설명 보기"):
    st.write("""
    이 프로젝트는 머신러닝 기반 Iris 꽃 분류 서비스입니다.

    ✔ 사용자가 꽃의 4가지 특징을 입력하면  
    ✔ 머신러닝 모델이 꽃 종류를 예측합니다  
    ✔ 예측 결과는 저장되어 통계로 시각화됩니다  
    ✔ 최근 기록도 확인할 수 있는 웹 서비스입니다  

    👉 Streamlit을 이용한 머신러닝 서비스 구현 프로젝트입니다.
    """)