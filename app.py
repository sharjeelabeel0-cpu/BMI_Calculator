
import streamlit as st

st.title("My BMI Calculator")
st.write("Enter your weight and height below.")

weight = st.number_input(
    "Weight (kg)",
    min_value=0.1,
    value=60.0
)

height = st.number_input(
    "Height (metres)",
    min_value=0.1,
    value=1.68
)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")
