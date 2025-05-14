import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.config import generate_text_response

def handle_text_input(model):
    """Handle all text input processing and display"""
    st.sidebar.header("Text Input")
    user_text = st.sidebar.text_area(
        "Enter your health goals, medical conditions, food preferences, etc.", 
        height=150
    )
    
    if user_text:
        with st.spinner("Generating personalized plan..."):
            try:
                response = generate_text_response(model, user_text)
                st.markdown("### 📄 Nutrition Plan")
                st.write(response)
            except Exception as e:
                st.error(f"Error generating nutrition plan: {e}")
                return False
        return True
    return False