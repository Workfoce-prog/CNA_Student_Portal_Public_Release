
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CNA Student Portal – Public Release")

df = pd.read_csv("student_data.csv")
st.write("Sample Student Data", df.head())

fig, ax = plt.subplots()
df['Risk_Score'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)
