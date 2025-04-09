import streamlit as st
import pandas as pd

st.title("📋 간단한 데이터 표시 앱")

# 예시 데이터프레임
data = {
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [23, 35, 29],
    '국가': ['한국', '한국', '한국']
}

df = pd.DataFrame(data)

# 데이터 출력
st.write(df)
