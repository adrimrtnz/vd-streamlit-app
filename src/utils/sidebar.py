import streamlit as st

def sidebar():
    """
    Renders the navigation sidebar for the Streamlit application.

    Includes links to all main pages of the application with appropriate labels
    and icons.
    """
    st.page_link(page='app.py', label='Home', icon=':material/home:')
    st.page_link(page='pages/plots.py', label='Plots', icon=':material/dataset:')
    st.page_link(page='pages/maps.py', label='Mapas y Vistas', icon=':material/map:')
    st.page_link(page='pages/investment_analysis.py', label='Análisis de Inversión', icon=':material/insights:')
    st.page_link(page='pages/timeline.py', label='Timeline', icon=':material/calendar_month:')
