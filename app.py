import streamlit as st
import sqlite3
import pandas as pd

# Page title
st.title("SQLizer – Text to SQL Assistant")
st.write("Ask questions in English and get results from the database")

# Input
question = st.text_input("Ask your question")

# Connect to SQLite DB
conn = sqlite3.connect("college.db")

def generate_sql(question):
    q = question.lower()

    if "only student names" in q or "student names" in q:
        return "SELECT name FROM students"

    elif "marks above" in q:
        number = ''.join(filter(str.isdigit, q))
        if number:
            return f"SELECT * FROM students WHERE marks > {number}"

    elif "all students" in q:
        return "SELECT * FROM students"

    else:
        return None

# Process question
if question:
    st.write("You asked:", question)

    sql = generate_sql(question)

    if sql:
        st.code(sql, language="sql")

        df = pd.read_sql(sql, conn)
        st.success("Query executed successfully")
        st.dataframe(df)

    else:
        st.warning("Sorry, I could not understand the question.")

conn.close()












