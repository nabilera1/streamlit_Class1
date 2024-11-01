# 예제 1
# import sqlite3
#
# # 데이터베이스 연결 (파일로 저장됨, 'mydb.db'가 파일명)
# conn = sqlite3.connect('mydb.db')
# cursor = conn.cursor()
#
# # 테이블 생성
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL
#     )
# ''')
#
# # 데이터 삽입
# cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
# cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
#
# # 변경 사항 저장
# conn.commit()
#
# # 데이터 조회
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
#
# for row in rows: # 터미널에서 보여짐
#     print(row)
#
# # 연결 종료
# conn.close()


# 예제 2

import sqlite3
import streamlit as st
import pandas as pd

# Streamlit 제목
st.title("SQLite Database with Streamlit")

# 데이터베이스 연결
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# 데이터 삽입 버튼
if st.button("Add Sample Data"):
    cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
    conn.commit()
    st.write("Sample data added!")

# 데이터 조회
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# 데이터프레임 변환 및 출력
df = pd.DataFrame(rows, columns=["ID", "Name", "Age"])
st.write("User Data from SQLite Database:")
st.dataframe(df)

# 연결 종료
conn.close()


