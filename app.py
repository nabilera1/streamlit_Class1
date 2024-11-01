import streamlit as st
import pandas as pd
import numpy as np

# 제목
st.title("Hello, Streamlit!")

# 슬라이더
number = st.slider("Pick a number", 0, 100)
st.write("Selected number:", number)

# 차트 예시 데이터 생성
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# 라인 차트
st.line_chart(chart_data)




