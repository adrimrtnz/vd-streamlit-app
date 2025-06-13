"""
Streamlit page for displaying Folium map visualizations related to AI publications
and investment. Users can select a map type from a dropdown menu.
Map rendering logic is handled by functions in `src/utils/data.py`.
"""
import streamlit as st
# streamlit_folium is imported here because it's a common dependency for map pages,
# though actual map rendering is delegated.
from streamlit_folium import st_folium

from utils.constants import options_dict_views
from utils.data import annual_papers_map_folium, annual_investment_map_folium
from utils.sidebar import sidebar

st.set_page_config(page_title='Mapas y Vistas',
                   layout='wide')
st.title('🌍 Mapas y Vistas')

with st.sidebar:
    sidebar()

options = st.selectbox(
    'Elige el gráfico que deseas visualizar',
    options=options_dict_views,
    label_visibility='collapsed',
    index=None,
    placeholder='Selecciona un mapa a visualizar...'
)

selected_idx = options_dict_views.get(options, None)

match selected_idx:
    case 0:
        annual_papers_map_folium()
    case 1:
        annual_investment_map_folium()