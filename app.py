# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
import os
import streamlit as st

# load_dotenv()

st.set_page_config(page_title = "Stream Chatbot",page_icon="🤖",layout = "wide",initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })