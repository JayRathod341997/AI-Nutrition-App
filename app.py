import streamlit as st
from utils.config import configure_gemini
from modules.text_input import handle_text_input 
from modules.image_input import handle_image_input 
# Initialize Gemini model
model = configure_gemini()

# Page config
st.set_page_config(page_title="AI Nutrition Assistant", layout="wide")
st.title("🥗 The Smartest AI Nutrition Assistant")

# Main content header
st.subheader("🍽️ Personalized Nutrition Insights")

# Process both input types
handle_text_input(model)
handle_image_input(model)