import streamlit as st

# 제목
st.title("Streamlit Button Example")

# 버튼 생성
if st.button("Click me!"):
    st.write("Button clicked!")
else:
    st.write("Button not clicked yet.")

# 조건에 따른 출력 예시
name = st.text_input("Enter your name:")
if st.button("Greet"):
    st.write(f"Hello, {name}!")
else:
    st.write("Enter your name and press 'Greet' to receive a greeting.")
