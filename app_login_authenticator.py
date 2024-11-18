# import streamlit as st
# import streamlit_authenticator as stauth
#
# # 사용자 정보 설정
# # 실제 환경에서는 사용자 정보를 암호화하여 데이터베이스 등에 저장하는 것이 좋습니다.
# names = ["John Doe", "Jane Doe"]
# usernames = ["johndoe", "janedoe"]
#
# # 비밀번호 해시 생성
# # 암호화된 비밀번호 목록 생성 (이 예제에서는 간단히 '123'과 '456'을 암호화한 것)
# passwords = ["123", "456"]
# hashed_passwords = stauth.Hasher(passwords).generate()
#
# # 인증기 생성
# authenticator = stauth.Authenticate(
#     names,
#     usernames,
#     hashed_passwords,
#     "my_cookie_name",      # 쿠키 이름
#     "my_signature_key",    # 임의의 서명 키
#     cookie_expiry_days=30  # 쿠키 만료일 설정 (예: 30일)
# )
#
# # 로그인 위젯
# name, authentication_status, username = authenticator.login("Login", "main")
#
# # 로그인 상태에 따른 화면 표시
# if authentication_status:
#     st.success(f"Welcome *{name}*!")
#     st.write("로그인 후 볼 수 있는 페이지입니다.")
#     authenticator.logout("Logout", "sidebar")  # 로그아웃 버튼을 사이드바에 추가
# elif authentication_status is False:
#     st.error("아이디나 비밀번호가 잘못되었습니다.")
# elif authentication_status is None:
#     st.warning("아이디와 비밀번호를 입력하세요.")

# 미해결된 상태
import streamlit as st
import streamlit_authenticator as stauth

# 사용자 정보 설정
names = ["John Doe", "Jane Doe"]
usernames = ["johndoe", "janedoe"]

# 비밀번호 목록 생성 및 개별 해싱
passwords = ["123", "456"]
hashed_passwords = [stauth.Hasher().hash(pw) for pw in passwords]

# 인증기 생성
authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "my_cookie_name",      # 쿠키 이름
    "my_signature_key",    # 임의의 서명 키
    cookie_expiry_days=30  # 쿠키 만료일 설정 (예: 30일)
)

# 로그인 위젯
name, authentication_status, username = authenticator.login("Login", "main")

# 로그인 상태에 따른 화면 표시
if authentication_status:
    st.success(f"Welcome *{name}*!")
    st.write("로그인 후 볼 수 있는 페이지입니다.")
    authenticator.logout("Logout", "sidebar")  # 로그아웃 버튼을 사이드바에 추가
elif authentication_status is False:
    st.error("아이디나 비밀번호가 잘못되었습니다.")
elif authentication_status is None:
    st.warning("아이디와 비밀번호를 입력하세요.")
