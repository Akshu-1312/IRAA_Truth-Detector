import streamlit as st

# Load your HTML file
with open("IRAA Truth Detector.html", 'r', encoding='utf-8') as f:
    html_content = f.read()

# Display the HTML
st.components.v1.html(html_content,height=600,scrolling=True)
