"""
Streamlit page for displaying various plots related to AI investment and publications.
Users can select a plot type from a dropdown menu, and the corresponding
visualization is rendered using functions from `src/utils/data.py`.
"""
import streamlit as st

from utils.constants import options_dict
from utils.sidebar import sidebar
from utils.data import annual_papers, global_investment

st.set_page_config(page_title='Plots',
                   layout='wide')
st.title('📊 Plots')

with st.sidebar:
    sidebar()

options = st.selectbox(
    'Elige el gráfico que deseas visualizar',
    options=options_dict,
    label_visibility='collapsed',
    index=None,
    placeholder='Selecciona un gráfico a visualizar...'
)

selected_idx = options_dict.get(options, None)

match selected_idx:
    case 0:
        global_investment()
    case 1:
        annual_papers()
