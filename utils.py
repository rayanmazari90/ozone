import streamlit as st
from streamlit_option_menu import option_menu




st.set_page_config(page_title=None, page_icon=None, layout="wide")

selected = option_menu(
    menu_title= None,
    options= ['Predictive Maintenance', 'Dashboard', 'Creators'],
    icons=['graph-up', 'clipboard-data'],
    menu_icon= "cast",
    default_index= 0,
    orientation='horizontal',)

if selected == 'Forecast':
    st.write('')
elif selected == 'Dashboard':
    pass

elif selected == 'Creators':
    pass