import streamlit as st

st.title('login')
id = st.text_input('ID')
pw = st.text_input('Password', type = 'password')
btn = st.button('LOGIN')
