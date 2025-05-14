import streamlit as st
from utils.config import configure_gemini
from modules.text_input import handle_text_input 
from modules.image_input import handle_image_input 
# Initialize Gemini model
model = configure_gemini()

st.set_page_config(page_title="AI Nutrition Assistant", layout="wide")
st.title("🥗 The Smartest AI Nutrition Assistant")

# Create tabs
tab1, tab2 = st.tabs(["📄 Nutrition Plan", "🧠 Food Analysis"])

# Process inputs in respective tabs
with tab1:
    st.subheader("Personalized Nutrition Plan")
    handle_text_input(model)

with tab2:
    st.subheader("Food Image Analysis")
    handle_image_input(model)