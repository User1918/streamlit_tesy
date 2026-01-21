import streamlit as st
import pandas as pd
if 'data' not in st.session_state:
    st.session_state.data = []
with st.form("employee_form"):
    age = st.text_input("Age: ")
    department = st.text_input("Department: ")
    gender = st.text_input("Gender: ")
    job_role = st.text_input("Job Role: ")
    MonthlyIncome = st.text_input("Monthly Income: ")
    clicked = st.form_submit_button("Submit")
    if clicked:
        st.session_state.data.append({
            'Age': age,
            'Department': department,
            'Gender': gender,
            'Job Role': job_role,
            'Monthly Income':MonthlyIncome
        })
        st.success("Data added successfully!")
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.table(df)