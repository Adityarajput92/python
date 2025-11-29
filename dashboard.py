import streamlit as st
import google.genai as genai
import pandas as pd
import matplotlib.pyplot as plt


with st.sidebar:
    st.title("MENU@H%")
    st.button("profile")
    st.button("new chat")
    st.button("library")
    st.button("history")
    st.button("help")
    st.button("logout")
    st.button("feedback")
    st.write("dashboard version 8 creators")



st.title("ai")
st.text("welcom to ai platform")


user_msg = st.text_input("Ask Anything:")


if st.button("send~"):
    if user_msg.strip() != "":
        with st.spinner("Geneating response..."):
            response = model.generate_content(user_msg)
        st.success(" bot responce:")
        st.write(response.text)
st.success("Dashboard loaded successfully!!!")