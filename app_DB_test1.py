import sqlite3
import streamlit as st
import pandas as pd

# Streamlit 제목
st.title("Add User to SQLite Database")

# 데이터베이스 연결
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 테이블 생성 (이미 존재하면 생략)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# 사용자 입력 폼
st.subheader("Enter User Information")
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, step=1)

# 데이터 삽입 버튼
if st.button("Add User"):
    if name and age:
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, int(age)))
        conn.commit()
        st.success(f"User '{name}' added successfully!")
    else:
        st.error("Please enter both name and age.")

# 데이터 조회 및 출력
st.subheader("User Data from SQLite Database")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=["ID", "Name", "Age"])
st.dataframe(df)

# 연결 종료
conn.close()
