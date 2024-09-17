import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')


st.sidebar.title('India data visualization')
selected_state = st.sidebar.selectbox('Select a State',list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('size represents primary parameter')
    st.text('color represents secondary parameter')
    if selected_state == 'Overall India':
        # plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",size=primary,color=secondary,
                                zoom=3, mapbox_style='carto-positron',size_max=35,width=1200,height=700,hover_name='District',color_continuous_scale='inferno')

        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude",size=primary,color=secondary,
                                zoom=6, mapbox_style='carto-positron',size_max=35,width=1200,height=700,hover_name='District',color_continuous_scale='inferno')
        st.plotly_chart(fig,use_container_width=True)
