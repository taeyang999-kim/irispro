import streamlit as st
from app.ml.predictor import predict_iris
from app.db.database import Database

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