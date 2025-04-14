import streamlit as st
import pandas as pd

def render():
    st.subheader("UFC - Predicción de Combates")

    fighter = st.text_input("Nombre del Luchador 1")
    opponent = st.text_input("Nombre del Luchador 2")

    if fighter and opponent:
        data = {
            "Opción": [f"Gana {fighter}", f"Gana {opponent}", "Over 1.5", "Under 1.5"],
            "Probabilidad (%)": [58, 42, 65, 35]
        }
        df = pd.DataFrame(data)
        st.dataframe(df)
