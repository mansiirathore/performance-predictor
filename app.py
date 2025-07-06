import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Student Score Predictor", layout="centered")

st.title("📊 Student Exam Score Predictor")
st.write("Enter your details below to predict your **Math score**:")

# Form
with st.form("predict_form"):
    gender = st.selectbox("Gender", ["male", "female"])
    ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parental_level_of_education = st.selectbox("Parental Education Level", [
        "associate's degree", "bachelor's degree", "high school",
        "master's degree", "some college", "some high school"
    ])
    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.number_input("Reading Score (out of 100)", min_value=0, max_value=100)
    writing_score = st.number_input("Writing Score (out of 100)", min_value=0, max_value=100)

    submitted = st.form_submit_button("Predict")

if submitted:
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )
        df = data.get_data_as_data_frame()
        predictor = PredictPipeline()
        result = predictor.predict(df)

        st.success(f"🎯 Predicted Math Score: **{result[0]:.2f}**")

    except Exception as e:
        st.error(f"❌ Error: {e}")
