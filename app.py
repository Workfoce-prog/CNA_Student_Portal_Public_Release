
import streamlit as st
import pandas as pd
from utils import check_login, get_recommendation
from translations import translate

# Simulated login (demo purpose)
if not check_login():
    st.stop()

# Load data
df = pd.read_csv("student_data.csv")

# Language selection
lang = st.selectbox("Choose language / Elige idioma", ["English", "Spanish"])

# Student selection
student_id = st.selectbox("Select your student ID", df["Student_ID"].unique())
student = df[df["Student_ID"] == student_id].iloc[0]

st.title(translate("CNA Readiness Dashboard", lang))
st.write(translate("Student Progress Summary", lang))

# Metrics display
for metric in ["Attendance", "Literacy_Score", "FRL_Status", "Food_Insecurity_Risk"]:
    st.metric(label=translate(metric, lang), value=student[metric])

# Recommendation
recommend = get_recommendation(student)
st.success(translate("Recommended Action:", lang) + " " + translate(recommend, lang))
