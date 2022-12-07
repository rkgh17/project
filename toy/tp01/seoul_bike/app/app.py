# -*- coding: utf-8 -*-

import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
from seoul_bike_app import run_seoul_bike_app

def main():

    with st.sidebar:
        selected = option_menu(None, ["Home", '따릉이'], 
        icons=['house', 'bicycle'], 
        menu_icon="list", 
        default_index=1, 
        styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#B8FFAA"},
        "nav-link-selected": {"font-size":"20px","background-color": "PaleGreen", "color":"black"}
        })
        # print(selected)
    
    if selected == "Home":
        home = Path("md/home.md").read_text(encoding='UTF-8')
        st.markdown(home, unsafe_allow_html=True)

    if selected == "따릉이":
        run_seoul_bike_app()

if __name__ == "__main__":
    main()