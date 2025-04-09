import streamlit as st
import pandas as pd

st.title("📊 Display Data App")

# 파일 업로드 받기
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # 데이터 읽기
    df = pd.read_csv(uploaded_file)

    st.subheader("데이터 미리보기")
    st.write(df.head())

    st.subheader("기본 정보")
    st.write(f"행 개수: {df.shape[0]}")
    st.write(f"열 개수: {df.shape[1]}")

    st.subheader("컬럼별 통계")
    st.write(df.describe())

    st.subheader("원하는 컬럼 선택해서 보기")
    columns = st.multiselect("컬럼 선택", df.columns.tolist())
    if columns:
        st.dataframe(df[columns])
else:
    st.warning("먼저 CSV 파일을 업로드하세요.")
