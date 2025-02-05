import streamlit as st
import pandas as pd
import numpy as np
if "students" not in st.session_state:
    st.session_state.students = []
st.title("Student Score Tracker")
st.header("Add Student")
name = st.text_input("Enter student name:")
score = st.number_input("Enter student score:", min_value=0, max_value=100, step=1)

if st.button("Add Student"):
    if name and score is not None:
        st.session_state.students.append({"Name": name, "Score": score})
        st.success(f"Added {name} with a score of {score}.")
    else:
        st.error("Please enter both a name and a score.")

# Convert data to a DataFrame for display
df = pd.DataFrame(st.session_state.students)

# Display student data
st.header("Student Data")
if not df.empty:
    st.dataframe(df)
else:
    st.write("No student data available.")

# Filter section
st.header("Filter Students by Minimum Score")
min_score = st.slider("Minimum score:", min_value=0, max_value=100, value=0)

# Filtered data
if not df.empty:
    filtered_df = df[df["Score"] >= min_score]
    st.subheader("Filtered Student Data")
    st.dataframe(filtered_df)
else:
    st.write("No student data available to filter.")
