
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("student_data.csv")

# UI
st.title("CNA Workforce Readiness Tracker for Underserved Communities")

# Select student ID
student_id = st.selectbox("Select Your Student ID", df["Student_ID"].unique())

# Filter data
student_data = df[df["Student_ID"] == student_id].iloc[0]

# Show student info
st.subheader("Student Information")
st.write(f"Name: {student_data['Name']}")
st.write(f"Age: {student_data['Age']}")
st.write(f"Gender: {student_data['Gender']}")
st.write(f"Region: {student_data['Region']}")

# Scores and RAG status
st.subheader("Skills Assessment")
scores = {
    "Digital Literacy": student_data["Digital_Literacy_Score"],
    "Workforce Readiness": student_data["Workforce_Readiness_Score"],
    "Health Knowledge": student_data["Health_Knowledge_Score"]
}
rag = {
    k: ("Green" if v >= 75 else "Amber" if v >= 50 else "Red")
    for k, v in scores.items()
}

# Display scores with RAG
for k, v in scores.items():
    st.write(f"{k}: {v} ({rag[k]})")

# Show pie chart
st.subheader("Score Distribution")
fig, ax = plt.subplots()
ax.pie(scores.values(), labels=scores.keys(), autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Trend chart placeholder (can be expanded with real longitudinal data)
st.subheader("Risk Trend Over Time (Example)")
trend_data = pd.DataFrame({
    "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
    "Score": [40, 55, 65, scores["Workforce Readiness"]]
})
st.line_chart(trend_data.set_index("Week"))

# Recommendation
st.subheader("Recommended Actions")
st.write(student_data["Recommendation_Action"])
