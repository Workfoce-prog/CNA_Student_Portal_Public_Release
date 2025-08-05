
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Language selection
lang = st.sidebar.selectbox("Choose Language / Choisissez la langue", ["English", "Français"])

# Multilingual text
text = {
    "English": {
        "title": "CNA Student Dashboard",
        "upload": "Upload Student Data CSV",
        "login": "Enter your student ID",
        "select": "Select your student ID",
        "analytics": "Student Analytics Dashboard"
    },
    "Français": {
        "title": "Tableau de bord étudiant CNA",
        "upload": "Télécharger le fichier CSV des étudiants",
        "login": "Entrez votre ID étudiant",
        "select": "Sélectionnez votre ID étudiant",
        "analytics": "Tableau de bord analytique étudiant"
    }
}

st.title(text[lang]["title"])

uploaded_file = st.file_uploader(text[lang]["upload"], type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "Student_ID" not in df.columns:
        st.error("Missing 'Student_ID' column.")
    else:
        student_id = st.selectbox(text[lang]["select"], df["Student_ID"].unique())
        student_data = df[df["Student_ID"] == student_id]

        st.subheader(text[lang]["analytics"])
        st.write(student_data)

        # Plotting attendance
        if "Attendance" in df.columns:
            st.altair_chart(alt.Chart(df).mark_bar().encode(
                x='Student_ID:N',
                y='Attendance:Q',
                tooltip=['Student_ID', 'Attendance']
            ).properties(title="Attendance by Student"))

        # Plotting performance if available
        if "Performance_Score" in df.columns:
            st.line_chart(df.set_index("Student_ID")["Performance_Score"])
