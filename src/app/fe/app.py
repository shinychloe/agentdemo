import streamlit as st
import requests

st.title("문서 요약 챗봇")

if prompt := st.chat_input("문서 내용을 요약해줘"):
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("요약 중..."):
            res = requests.post("http://localhost:8000/complete", json={})
            answer = res.json().get("answer", "")
            st.write(answer)