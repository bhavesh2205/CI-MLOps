import streamlit as st


def calculate_bmi(weight, height):
    """Calculate BMI and return category."""
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive numbers.")

    bmi = weight / (height**2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


# Streamlit App
st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.0, format="%.2f")

if st.button("Calculate"):
    try:
        bmi, category = calculate_bmi(weight, height)
        st.success(f"Your BMI is {bmi:.2f}, which is categorized as {category}.")
    except ValueError as e:
        st.error(str(e))
