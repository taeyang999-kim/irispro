import streamlit as st
import pandas as pd
import altair as alt

# 1. SESSION STATE DB (중요)
if "data" not in st.session_state:
    st.session_state.data = []


class Database:
    def save_iris(self, sl, sw, pl, pw, result):
        st.session_state.data.append({
            "Sepal Length": sl,
            "Sepal Width": sw,
            "Petal Length": pl,
            "Petal Width": pw,
            "Result": result
        })

    def get_data(self):
        return st.session_state.data

    def get_result_stats(self):
        stats = {"Setosa": 0, "Versicolor": 0, "Virginica": 0}

        for d in st.session_state.data:
            stats[d["Result"]] += 1

        return stats


db = Database()


# 2. ML MODEL (RULE BASED)
def predict_iris(features):
    sl, sw, pl, pw = features

    if pl < 2:
        return "Setosa"
    elif pl < 5:
        return "Versicolor"
    else:
        return "Virginica"


# 3. PAGE CONFIG (최상단 안전)
st.set_page_config(
    page_title="Iris ML Service",
    page_icon="🌸",
    layout="centered"
)

st.title("🌸 Iris Flower Classification Service")
st.caption("Machine Learning 기반 꽃 종류 예측 웹 애플리케이션")

st.markdown("---")


# 4. INPUT UI
st.subheader("📥 꽃 정보 입력")

col1, col2 = st.columns(2)

with col1:
    sl = st.number_input("Sepal Length", value=5.0)
    sw = st.number_input("Sepal Width", value=3.0)

with col2:
    pl = st.number_input("Petal Length", value=1.5)
    pw = st.number_input("Petal Width", value=0.2)

if st.button("🌸 Predict Species"):

    result = predict_iris([sl, sw, pl, pw])
    db.save_iris(sl, sw, pl, pw, result)

    st.success(f"Prediction: {result}")
    st.metric("Predicted Class", result)


st.markdown("---")


# 5. STATISTICS
st.subheader("📊 Prediction Statistics")

stats = db.get_result_stats()

if sum(stats.values()) > 0:
    st.bar_chart(stats)
else:
    st.warning("아직 예측 데이터가 없습니다.")


# 6. RECENT DATA
st.subheader("📋 Recent Predictions")

df = pd.DataFrame(db.get_data())

if not df.empty:
    st.dataframe(df.tail(10))
else:
    st.info("아직 데이터가 없습니다.")


# 7. CSV / EXCEL UPLOAD + GRAPH
st.markdown("---")
st.subheader("📂 CSV / Excel 데이터 분석")

uploaded_file = st.file_uploader(
    "CSV 또는 Excel 파일 업로드",
    type=["csv", "xlsx"]
)

upload_df = None

if uploaded_file is not None:

    # 파일 읽기
    if uploaded_file.name.endswith(".csv"):
        upload_df = pd.read_csv(uploaded_file)
    else:
        upload_df = pd.read_excel(uploaded_file)

    st.success("파일 업로드 성공!")
    st.dataframe(upload_df)

    st.markdown("### 📊 XY Scatter Plot")

    col_x = st.selectbox("X축 선택", upload_df.columns)
    col_y = st.selectbox("Y축 선택", upload_df.columns)

    color_col = "Result" if "Result" in upload_df.columns else None

    if st.button("📈 산점도 생성"):

        if color_col:
            chart = alt.Chart(upload_df).mark_circle(size=80).encode(
                x=col_x,
                y=col_y,
                color=color_col,
                tooltip=list(upload_df.columns)
            ).interactive()

            st.altair_chart(chart, use_container_width=True)

        else:
            st.scatter_chart(upload_df[[col_x, col_y]])


# 8. RESET
if st.button("🧹 Reset All Data"):
    st.session_state.data.clear()
    st.success("모든 데이터 초기화 완료")
    st.rerun()

# 9. DESCRIPTION
with st.expander("📘 프로젝트 설명"):
    st.write("""
    - Iris 꽃 분류 ML 서비스
    - 입력값 기반 예측
    - 결과 저장 및 통계
    - CSV 업로드 분석 기능
    - XY Scatter Plot 시각화
    """)