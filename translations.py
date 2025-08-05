
def translate(text, lang):
    dictionary = {
        "CNA Readiness Dashboard": {"Spanish": "Panel de preparación de CNA"},
        "Student Progress Summary": {"Spanish": "Resumen del progreso del estudiante"},
        "Attendance": {"Spanish": "Asistencia"},
        "Literacy_Score": {"Spanish": "Puntaje de alfabetización"},
        "FRL_Status": {"Spanish": "Estado de almuerzo gratuito/reducido"},
        "Food_Insecurity_Risk": {"Spanish": "Riesgo de inseguridad alimentaria"},
        "Recommended Action:": {"Spanish": "Acción recomendada:"},
        "Refer to food bank and nutrition services": {"Spanish": "Referir a banco de alimentos y servicios de nutrición"},
        "Schedule counselor check-in": {"Spanish": "Programar sesión con consejero"},
        "Continue regular check-ins": {"Spanish": "Continuar con sesiones regulares"}
    }
    return dictionary.get(text, {}).get(lang, text)
