import streamlit as st
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