import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(
    page_title="SQLizer – Text to SQL Assistant",
    layout="wide"
)

st.title("SQLizer – Text to SQL Assistant")
st.write("Ask questions in English and get results from the database")

# ---------- DATABASE CONNECTION ----------
import sqlite3

def get_connection():
    return sqlite3.connect("college.db")

# ---------- TEXT → SQL ----------
def generate_sql(question: str):
    q = question.lower()

    # only names
    if "name" in q or "names" in q:
        if "only" in q or "show" in q:
            return "SELECT name FROM students"

    # marks above
    if "above" in q:
        number = int("".join(filter(str.isdigit, q)))
        return f"SELECT * FROM students WHERE marks > {number}"

    # marks below
    if "below" in q:
        number = int("".join(filter(str.isdigit, q)))
        return f"SELECT * FROM students WHERE marks < {number}"

    # highest marks
    if "highest" in q or "topper" in q or "top" in q:
        return "SELECT * FROM students ORDER BY marks DESC LIMIT 1"

    # lowest marks
    if "lowest" in q:
        return "SELECT * FROM students ORDER BY marks ASC LIMIT 1"

    # fallback
    return "SELECT * FROM students"

# ---------- UI ----------
question = st.text_input("Ask your question")

if st.button("Run Query") and question:
    sql_query = generate_sql(question)

    st.subheader("Generated SQL")
    st.code(sql_query, language="sql")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        if rows:
            df = pd.DataFrame(rows, columns=columns)
            st.success("Query executed successfully ✅")
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("No results found")

        cursor.close()
        conn.close()

    except Exception as e:
        st.error(e)









