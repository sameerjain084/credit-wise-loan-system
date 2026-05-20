import streamlit as st

# Title
st.title("CreditWise Loan Prediction System")

st.write("Enter applicant details below")

# Inputs
income = st.number_input("Applicant Income")
loan_amount = st.number_input("Loan Amount")
credit_history = st.selectbox("Credit History", [0, 1])

# Prediction button
if st.button("Predict Loan Status"):

    # Beginner dummy logic
    if credit_history == 1 and income > loan_amount:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")