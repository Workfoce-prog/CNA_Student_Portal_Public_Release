
import streamlit as st

def check_login():
    return True  # Placeholder for login

def get_recommendation(student):
    if student["Food_Insecurity_Risk"] > 0.7:
        return "Refer to food bank and nutrition services"
    elif student["Attendance"] < 0.8:
        return "Schedule counselor check-in"
    else:
        return "Continue regular check-ins"
