
import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Page config
st.set_page_config(page_title="AI Nutrition Assistant", layout="wide")
st.title("🥗 The Smartest AI Nutrition Assistant")

# Sidebar layout
st.sidebar.header("User Input")
user_text = st.sidebar.text_area("Enter your health goals, medical conditions, food preferences, etc.", height=150)
uploaded_image = st.sidebar.file_uploader("Upload a food image or grocery label", type=["jpg", "jpeg", "png"])

# Output area
st.subheader("🍽️ Personalized Nutrition Insights")

if user_text:
    with st.spinner("Generating personalized plan..."):
        try:
            response = model.generate_content(user_text)
            st.markdown("### 📄 Nutrition Plan")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing image and generating nutrition insights..."):
        try:
            response = model.generate_content(["Analyze this image and describe the food content with nutrition details", image])
            st.markdown("### 🧠 Food Analysis")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
