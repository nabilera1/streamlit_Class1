import streamlit as st

# Streamlit 세션 상태 초기화
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# 로그인 함수 정의
def login():
    if id == "admin" and pw == "password":  # 예시로 ID와 PW를 'admin'과 'password'로 설정
        st.session_state["logged_in"] = True
        st.success("로그인에 성공했습니다!")
        st.experimental_rerun()  # 로그인 후 화면을 새로 고침하여 대시보드로 이동
    else:
        st.error("ID 또는 Password가 올바르지 않습니다.")

# 로그아웃 함수 정의
def logout():
    st.session_state["logged_in"] = False
    st.info("로그아웃되었습니다.")
    st.experimental_rerun()  # 로그아웃 후 화면을 새로 고침하여 로그인 화면으로 이동

# 로그인 화면
if not st.session_state["logged_in"]:
    st.title("Login")
    id = st.text_input("ID")
    pw = st.text_input("Password", type="password")
    if st.button("LOGIN"):
        login()

# 로그인 후 화면
else:
    st.title("Welcome")
    st.write("로그인 후에만 볼 수 있는 내용을 표시합니다.")
    if st.button("LOGOUT"):
        logout()
