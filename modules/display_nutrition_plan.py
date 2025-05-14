import streamlit as st
import re

def display_nutrition_plan(response_text):
    # Split the response into days
    day_sections = re.split(r'=== Day \d+ ===', response_text)
    
    # Create tabs for each day
    if len(day_sections) > 1:
        tab_titles = [f"Day {i+1}" for i in range(7)]
        tabs = st.tabs(tab_titles)
        
        for i, tab in enumerate(tabs):
            with tab:
                if i < len(day_sections)-1:
                    day_content = day_sections[i+1].strip()
                    st.markdown(f"### 🍽️ Day {i+1} Meal Plan")
                    
                    # Format the content with proper spacing
                    formatted_content = day_content.replace(' - ', '\n\n- ')
                    st.markdown(formatted_content)
                    
                    # Add download button for each day
                    st.download_button(
                        label=f"Download Day {i+1} Plan",
                        data=day_content,
                        file_name=f"nutrition_plan_day_{i+1}.txt",
                        mime="text/plain"
                    )
                else:
                    st.write("Content not available for this day")
    else:
        st.write(response_text)  # Fallback if parsing fails

# In your main function where you display the response:
