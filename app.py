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
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Iloveme@09",
        database="college"
    )

# ---------- TEXT → SQL ----------
import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_sql(question):
    prompt = f"""
You are an expert SQL generator.

Database: MySQL
Table: students(id, name, marks)

Rules:
- Output ONLY SQL
- No explanation
- No markdown
- No backticks

User question:
{question}
"""

    response = model.generate_content(prompt)
    return response.text.strip()









