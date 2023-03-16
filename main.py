import streamlit as st

def hba1c_to_eag(hba1c):
    """Converts HbA1C value to Estimated Average Glucose (eAG)"""
    eag = (hba1c * 28.7) - 46.7
    return eag

st.title("HbA1C to eAG Calculator")

st.write("Enter your HbA1C value to calculate your estimated average glucose (eAG):")

hba1c = st.number_input("HbA1C")

if st.button("Calculate eAG"):
    eag = hba1c_to_eag(hba1c)
    st.write(f"Your estimated average glucose (eAG) is: {eag} mg/dL")
