import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(layout = "centered")
page = st.sidebar.selectbox('Select page',['Ankieta','Staty']) 

if page == 'Ankieta':
    firstname = st.text_input("Please, enter your 1st name", "Type here...")
    secondname = st.text_input("Please, enter your 2nd name", "Type here...")
    if st.button("Submit"):
        st.success("Prawidłowo zapisano")

if page == 'Staty':
    data = st.file_uploader("Upload your dataset", type=['csv'])
    if data is not None:
        with st.spinner("Waiting..."):
            time.sleep(2)
        st.success("Finished!")
        df = pd.read_csv(data)
        st.dataframe(df.head(10))

        st.set_option('deprecation.showPyplotGlobalUse', False)
        all_columns_names = df.columns.to_list()
        selected_chart = st.selectbox("Select type of chart", ['Bar chart', 'Line Chart'])
        if selected_chart == 'Bar chart':
            selected_column_names = st.multiselect("Select columns to plot", all_columns_names)
            plot_data = df[selected_column_names]
            st.bar_chart(plot_data)

        if selected_chart == 'Line Chart':
            selected_column_names = st.multiselect("Select columns to plot", all_columns_names)
            plot_data = df[selected_column_names]
            st.line_chart(plot_data)