
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Title
st.title("CNA Student Portal – Public Release")

# Load data
df = pd.read_csv("student_progress_data.csv")

# Select student
student_id = st.selectbox("Select Student ID", df["Student_ID"].unique())
student_data = df[df["Student_ID"] == student_id]

# Display student metrics
st.subheader("Student Metrics")
st.write(student_data)

# Progress Chart
st.subheader("Progress Chart")
fig, ax = plt.subplots()
ax.plot(student_data["Week"], student_data["Score"], marker="o")
ax.set_title("Score Over Time")
ax.set_xlabel("Week")
ax.set_ylabel("Score")
st.pyplot(fig)

# Altair bar chart for RAG status
st.subheader("RAG Status")
rag_chart = alt.Chart(student_data).mark_bar().encode(
    x='Status',
    y='count()',
    color='Status'
).properties(width=300)
st.altair_chart(rag_chart)

# Recommendations
st.subheader("Actionable Recommendations")
st.write(student_data["Recommendation_Action"].values[0])
