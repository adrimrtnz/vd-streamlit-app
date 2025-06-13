import os
import streamlit as st
from streamlit_timeline import timeline


from utils.sidebar import sidebar
from utils.config import DATA_PATH, TIMELINE_DATA


st.set_page_config(page_title='Timeline',
                   layout='wide')
st.title('📅 Timeline')

with st.sidebar:
    sidebar()

# Load timeline data from JSON file
data_path = os.path.join(DATA_PATH, TIMELINE_DATA)
try:
    with open(data_path, 'r', encoding='utf-8') as f: # Added encoding
        data = f.read()
except FileNotFoundError:
    st.error(f"Error: Timeline data file not found at {data_path}")
    data = None
except Exception as e:
    st.error(f"Error loading timeline data: {e}")
    data = None

# Add a slider to control the timeline height
timeline_height = st.slider(
    "Ajustar Altura de la Línea de Tiempo (px)",
    min_value=400,
    max_value=1500,
    value=800, # New default height
    step=50
)

if data:
    timeline(data, height=timeline_height)
else:
    st.warning("No timeline data to display.")