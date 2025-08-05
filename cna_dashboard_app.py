
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CNA Student Portal", layout="wide")

st.title("📘 CNA Workforce Readiness Student Portal")

df = pd.read_csv("data/student_data.csv")

student_id = st.selectbox("Select Your Student ID", df["Student_ID"].unique())
student_data = df[df["Student_ID"] == student_id].iloc[0]

st.subheader("📊 Your Metrics Tracker")
cols = st.columns(3)
cols[0].metric("Quiz Score", f"{student_data['Quiz_Score']}%", delta=None)
cols[1].metric("Progress", student_data['Progress_Level'])
cols[2].metric("Status", student_data['RAG_Status'])

st.subheader("📈 Risk Trend Over Time")
trend = df[df["Student_ID"] == student_id][['Week_1', 'Week_2', 'Week_3', 'Week_4']]
plt.plot(trend.columns, trend.values.flatten(), marker='o')
plt.title("Student Risk Trend")
plt.xlabel("Week")
plt.ylabel("Score")
st.pyplot(plt)

st.subheader("🧠 Quick Recap Quiz")
st.write("Q: What is a vital sign you should always check during patient intake?")
answer = st.radio("Select one", ["Height", "Blood Pressure", "Vision", "Hair Color"])
if answer:
    if answer == "Blood Pressure":
        st.success("Correct!")
    else:
        st.error("Try again!")

st.subheader("📝 Recommendation")
st.info(student_data["Recommendation"])
