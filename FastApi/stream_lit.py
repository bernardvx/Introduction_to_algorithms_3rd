import streamlit as st
import json
import requests


backend_url = "http://fastapi:8000"

st.title("fastapi Youtube")

option = st.selectbox("What you want to do?",
                      ("Create User", "Show my videos", "Upload Videos"))


if "Create User" in option:
    st.write("you  want to create a new user: ", option)
    name  = st.text_input("Name")
    if name:
        response = requests.post(f"{backend_url}/users/", json={"name": name})
        if response.status_code == 200:
            st.write("You have added a new user", response.json())
        else:
            st.error("Error adding a new user")
            st.write(response.json())


if "Show my videos" in option:
    user_id = st.text_input("Your user id")
    if user_id:
        response = requests.get(f"{backend_url}/users/{user_id}")
        if response.status_code == 200:
            st.write("These are your videos", response.json())
        else:
            st.error("Error showing your videos")
            st.write(response.json())

if "Upload Videos" in option:
    owner_id = st.text_input("Your user id")
    video_url = st.text_input("Your video url")
    if video_url:
        response = requests.post(f"{backend_url}/users/{owner_id}/videos", json={"user_id": owner_id, "url": video_url})
        if response.status_code == 200:
            st.write("video uploaded", response.json())
        else:
            st.error("Error uploading your video")
            st.write(response.json())



