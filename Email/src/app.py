import streamlit as st

from utils.helpers import insert, fetch, update, delete 

st.header("Welcme to our Email manager app!")
st.subheader("Please choose your desired page from the sidebar")

pages = {
    "User Profile": "pages/01_UserProfile.py",
    "Email Profiles": "pages/02_Profiles.py",
    "Templates": "pages/03_Templates.py",
    "History": "pages/04_send_email.py",
    "Scheduler": "pages/05_Scheduler.py",
    "History": "pages/06_History.py",
    "Chatbot": "pages/07_Chatbot.py",
}


































































