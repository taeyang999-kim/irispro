# 🔥 7. CSV / Excel 업로드 + 시각화 기능 추가
st.markdown("---")
st.subheader("📂 CSV / Excel 데이터 분석")

uploaded_file = st.file_uploader(
    "CSV 또는 Excel 파일을 업로드하세요",
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

    # 컬럼 선택
    col1 = st.selectbox("X축 선택", upload_df.columns)
    col2 = st.selectbox("Y축 선택", upload_df.columns)

    # 색 기준 (있으면 자동 사용)
    color_col = None
    if "Result" in upload_df.columns:
        color_col = "Result"

    # 그래프 버튼
    if st.button("📈 산점도 생성"):

        if color_col:
            import altair as alt

            chart = alt.Chart(upload_df).mark_circle(size=80).encode(
                x=col1,
                y=col2,
                color=color_col,
                tooltip=list(upload_df.columns)
            ).interactive()

            st.altair_chart(chart, use_container_width=True)

        else:
            st.scatter_chart(upload_df[[col1, col2]])