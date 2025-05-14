import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.config import generate_text_response

def handle_text_input(model):
    """Handle all text input processing and display"""
    with st.expander("➕ Provide Your Details", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            # Personal Details
            st.subheader("Personal Information")
            age = st.number_input("Age", min_value=1, max_value=120, value=30)
            gender = st.selectbox("Gender", ["Male", "Female"])
            cultural_background = st.text_input("Cultural/Ethnic Background")
            lifestyle = st.selectbox("Lifestyle", ["Sedentary", "Moderately Active", "Very Active", "Athlete"])
            
            # Health Conditions
            st.subheader("Health Information")
            medical_conditions = st.text_area("Medical Conditions (e.g. diabetes, hypertension)")
            allergies = st.text_area("Food Allergies/Intolerances")
            medications = st.text_area("Current Medications")
            
        with col2:
            # Goals & Preferences
            st.subheader("Goals & Preferences")
            health_goals = st.multiselect(
                "Primary Health Goals",
                options=[
                    "Weight loss",
                    "Muscle gain",
                    "Improved digestion",
                    "Heart health",
                    "Diabetes management",
                    "Increased energy",
                    "Better sleep",
                    "Stress reduction",
                    "Improved athletic performance",
                    "Hormonal balance",
                    "Cholesterol management",
                    "Blood pressure control",
                    "Anti-inflammatory diet",
                    "Pregnancy nutrition",
                    "Postpartum recovery",
                    "Menopause support"
                ],
                default=["Weight loss"],
                help="Select all that apply"
            )
            fitness_routine = st.selectbox(
                "Current Fitness Routine",
                ["No exercise", "Light exercise", "Moderate exercise", "Intense exercise"]
            )
            dietary_preferences = st.multiselect(
                "Dietary Preferences",
                ["Vegetarian", "Vegan", "Pescatarian", "Gluten-free", 
                 "Dairy-free", "Keto", "Mediterranean", "Other"]
            )
            other_preferences = st.text_area("Other Food Preferences/Aversions")
            cooking_ability = st.select_slider("Cooking Skill Level", ["Beginner", "Intermediate", "Advanced"])
    
    if st.button("Generate Personalized Nutrition Plan", type="primary"):
        if not health_goals:
            st.warning("Please at least specify your health goals")
        else:
            with st.spinner("Creating your holistic nutrition plan..."):
                try:
                    # Construct comprehensive prompt
                    prompt = f"""
                    Create a detailed, personalized nutrition plan for:
                    - Age: {age}
                    - Gender: {gender}
                    - Cultural background: {cultural_background}
                    - Lifestyle: {lifestyle}
                    - Medical conditions: {medical_conditions}
                    - Allergies/Intolerances: {allergies}
                    - Medications: {medications}
                    - Health goals: {health_goals}
                    - Fitness routine: {fitness_routine}
                    - Dietary preferences: {', '.join(dietary_preferences)}
                    - Other preferences: {other_preferences}
                    - Cooking ability: {cooking_ability}

                    The plan should:
                    1. Address all health conditions and medications
                    2. Respect cultural food preferences
                    3. Align with stated lifestyle and fitness routine
                    4. Provide meal suggestions matching cooking ability
                    5. Include nutrient timing recommendations
                    6. Suggest alternatives for allergies
                    7. Address the stated health goals
                    8. Provide gradual improvement phases
                    9. Include hydration recommendations
                    10. Suggest supplements if appropriate

                    Format the plan with clear sections and practical advice.
                    """
                    
                    response = generate_text_response(model, prompt)
                    st.markdown("## 🌿 Your Holistic Nutrition Plan")
                    st.markdown("---")
                    st.write(response)
                except Exception as e:
                    st.error(f"Error generating plan: {e}")
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