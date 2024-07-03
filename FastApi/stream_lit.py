import streamlit as st
import json
import requests


backend_url = "http://127.0.0.1:8000"

st.title("fastapi Youtube")

option = st.selectbox("What you want to do?",
                      ("Create User", "Show my videos", "Upload Videos"))


if "Create User" in option:
    st.write("you  want to create a new user: ", option)

#st.write("you selected: ", option)



