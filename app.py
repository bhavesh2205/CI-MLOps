import streamlit as st


def calculate_bmi(weight, height):
    """Calculate BMI and return the category."""
    if height <= 0 or weight <= 0:
        return None, "Invalid input! Weight and height must be positive numbers."

    bmi = weight / (height**2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2), category


# Streamlit UI
st.title("BMI Calculator")

st.write("Enter your weight and height to calculate your BMI.")

# Input fields
weight = st.number_input("Enter your weight (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    try:
        bmi, category = calculate_bmi(weight, height)
        st.success(f"Your BMI is **{bmi}**")
        st.info(f"Category: **{category}**")
    except ValueError as e:
        st.error(str(e))
