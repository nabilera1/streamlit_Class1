import streamlit as st
import pandas as pd

st.title("📂 구글 드라이브 엑셀 불러오기")

# 예시 구글 드라이브 공유 링크
# url = st.text_input("구글 드라이브 공유 링크를 입력하세요:")
url = "https://docs.google.com/spreadsheets/d/1XIWlTtMlsL07eoyJf8sbf7SjJWXBZxd2/edit?usp=sharing&ouid=102499631843628462810&rtpof=true&sd=true"
if url:
    try:
        # 공유 링크를 다운로드 링크로 변환
        file_id = url.split("/d/")[1].split("/")[0]
        download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

        # 엑셀 파일 읽기
        df = pd.read_excel(download_url)

        st.success("엑셀 파일을 성공적으로 불러왔어요!")
        st.dataframe(df)
    except Exception as e:
        st.error(f"파일을 불러오는 데 실패했어요: {e}")
