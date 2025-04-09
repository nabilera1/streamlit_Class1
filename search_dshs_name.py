import streamlit as st
import pandas as pd

st.title("사용자 ID / 비밀번호 조회")
st.info("금요일 이후 이 사이트는 사라짐. \n 아이디 비번 메모 및 비밀번호는 처음 접속 후 변경을 권장합니다.")


st.markdown("""
---

### 🔍 [검수 완료를 위한 테스트 방법]  
- **ChatGPT 접속 사이트**  
👉 [https://chatgpt.com/](https://chatgpt.com/)

---

### 🔐 [인증코드 요구시 참고 사이트]  
- 처음 접속 시 인증코드를 요청하면 **mygpt.kr** 사이트에 아래 아이디로 로그인하면 됩니다.  
  - **아이디**: `dshs04`  
  - **비밀번호**: 위와 동일  
  👉 [https://www.mygpt.kr/](https://www.mygpt.kr/)

---
""")


# 엑셀 파일 경로 or 구글 드라이브 URL
url = "https://docs.google.com/spreadsheets/d/1XIWlTtMlsL07eoyJf8sbf7SjJWXBZxd2/edit?usp=sharing&ouid=102499631843628462810&rtpof=true&sd=true"

if url:
    try:
        # 구글 드라이브 ID 추출 및 다운로드 링크 생성
        file_id = url.split("/d/")[1].split("/")[0]
        download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

        # 엑셀 데이터 읽기
        df = pd.read_excel(download_url)

        # 이름 검색 입력창
        name = st.text_input("이름을 입력하세요:")

        if name:
            result = df[df["이름"] == name]

            if not result.empty:
                st.success("검색 결과")
                st.write(f"🆔 ID: `{result.iloc[0]['ID']}`")
                st.write(f"🔑 비밀번호: `{result.iloc[0]['비밀번호']}`")
            else:
                st.warning("일치하는 이름이 없습니다.")
    except Exception as e:
        st.error(f"파일을 불러오는 데 실패했어요: {e}")

