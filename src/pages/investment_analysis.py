"""
Streamlit page for comparative analysis of AI investment data.
This page displays trends in Global Generative AI investment and Total Private AI
investment, both as separate charts and as a combined comparison for 'World' data.
Data is loaded using functions from `src.utils.data`.
"""
import streamlit as st
import plotly.express as px
import pandas as pd # Import pandas
from utils.data import load_global_investment_data, load_private_ai_investment_data
from utils.sidebar import sidebar

# Page configuration
st.set_page_config(page_title='Análisis de Inversión', layout='wide')

# Title
st.title('📊 Análisis Comparativo de Inversión en IA')

# Sidebar
with st.sidebar:
    sidebar()

# Load data
try:
    df_global_gen_ai = load_global_investment_data()
    df_private_ai = load_private_ai_investment_data()

    # Remove placeholder dataframes (or comment them out)
    # st.subheader("Inversión Global en IA Generativa (Datos Muestra)")
    # if df_global_gen_ai is not None and not df_global_gen_ai.empty:
    #     st.dataframe(df_global_gen_ai.head())
    # else:
    #     st.warning("No se pudieron cargar los datos de inversión global en IA generativa.")

    # st.subheader("Inversión Privada Total en IA (Datos Muestra)")
    # if df_private_ai is not None and not df_private_ai.empty:
    #     st.dataframe(df_private_ai.head())
    # else:
    #     st.warning("No se pudieron cargar los datos de inversión privada total en IA.")

    # Side-by-side line charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Tendencia de Inversión Global en IA Generativa")
        if df_global_gen_ai is not None and not df_global_gen_ai.empty:
            fig_global = px.line(df_global_gen_ai, x='Year', y='Investment', color='Entity',
                                 title='Inversión Global en IA Generativa', markers=True,
                                 labels={'Investment': 'Inversión (Billones USD)', 'Year': 'Año'})
            fig_global.update_layout(yaxis_title='Inversión (Billones USD)')
            st.plotly_chart(fig_global, use_container_width=True)
        else:
            st.warning("Datos de inversión global en IA generativa no disponibles.")

    with col2:
        st.subheader("Tendencia de Inversión Privada Total en IA")
        if df_private_ai is not None and not df_private_ai.empty:
            fig_private = px.line(df_private_ai, x='Year', y='Investment', color='Entity',
                                  title='Inversión Privada Total en IA', markers=True,
                                  labels={'Investment': 'Inversión (Billones USD)', 'Year': 'Año'})
            fig_private.update_layout(yaxis_title='Inversión (Billones USD)')
            st.plotly_chart(fig_private, use_container_width=True)
        else:
            st.warning("Datos de inversión privada total en IA no disponibles.")

    st.divider() # Visual separator

    # Combined Line Chart for 'World' Entity
    st.subheader("Comparación Directa: Inversión Mundial Total")

    # Check if both main dataframes are loaded
    if df_global_gen_ai is not None and not df_global_gen_ai.empty and \
       df_private_ai is not None and not df_private_ai.empty:

        # Filter for 'World' entity and rename columns for clarity in the merged chart
        df_global_world = df_global_gen_ai[df_global_gen_ai['Entity'] == 'World'].copy()
        df_global_world.rename(columns={'Investment': 'Inversión IA Generativa (Billones USD)'}, inplace=True)

        df_private_world = df_private_ai[df_private_ai['Entity'] == 'World'].copy()
        df_private_world.rename(columns={'Investment': 'Inversión Privada Total IA (Billones USD)'}, inplace=True)

        # Proceed only if data for 'World' exists in both dataframes
        if not df_global_world.empty and not df_private_world.empty:
            # Merge the two 'World' datasets on 'Year'
            # Using an outer merge to include all years from both datasets
            df_world_comparison = pd.merge(
                df_global_world[['Year', 'Inversión IA Generativa (Billones USD)']],
                df_private_world[['Year', 'Inversión Privada Total IA (Billones USD)']],
                on='Year',
                how='outer'
            ).sort_values('Year')

            # Melt the DataFrame for Plotly Express:
            # This transforms the data from wide format (separate columns for each investment type)
            # to long format (one column for investment type, one for investment value).
            df_melted = df_world_comparison.melt(
                id_vars=['Year'],
                value_vars=['Inversión IA Generativa (Billones USD)', 'Inversión Privada Total IA (Billones USD)'],
                var_name='Tipo de Inversión',
                value_name='Inversión (Billones USD)'
            )

            # Drop rows where 'Inversión (Billones USD)' is NaN, which can result from the outer merge
            # if one dataset has years the other doesn't.
            df_melted.dropna(subset=['Inversión (Billones USD)'], inplace=True)

            if not df_melted.empty:
                fig_comparison = px.line(
                    df_melted,
                    x='Year',
                    y='Inversión (Billones USD)',
                    color='Tipo de Inversión',
                    title='Inversión Mundial: IA Generativa vs. Privada Total',
                    markers=True,
                    labels={'Inversión (Billones USD)': 'Inversión (Billones USD)', 'Year': 'Año'}
                )
                fig_comparison.update_layout(yaxis_title='Inversión (Billones USD)')
                st.plotly_chart(fig_comparison, use_container_width=True)
            else:
                st.warning("No hay datos coincidentes por año para la comparación mundial.")
        else:
            st.warning("No se encontraron datos para la entidad 'World' en uno o ambos conjuntos de datos para la comparación.")
    else:
        st.warning("Uno o ambos conjuntos de datos principales no están disponibles para la comparación mundial.")

except Exception as e:
    st.error(f"Ocurrió un error al cargar o procesar los datos para la página: {e}")
    # Optionally, display more detailed error information for debugging
    # import traceback
    # st.text(traceback.format_exc())
