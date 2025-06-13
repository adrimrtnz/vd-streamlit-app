"""
Main application file for the Streamlit AI Dashboard.

This page serves as the home page, displaying a header image and the content
from the project's README.md file. It also initializes the common sidebar.
"""
import streamlit as st

from utils.sidebar import sidebar

# Configure the page
st.set_page_config(page_title='Home', layout='wide') # Added layout='wide' for consistency


try:
    st.image('src/img/main_header.png')
except FileNotFoundError:
    st.error("Header image (src/img/main_header.png) not found. Ensure the path is correct relative to the app's root directory when running Streamlit.")


# Load and display content from README.md
try:
    with open('README.md', 'r', encoding='utf-8') as f: # Added encoding
        readme_content = f.read()
    st.markdown(readme_content)
except FileNotFoundError:
    st.error("README.md not found. Please ensure it is in the parent directory of 'src'.")
except Exception as e:
    st.error(f"Error reading README.md: {e}")


# Initialize the sidebar
with st.sidebar:
    sidebar()
