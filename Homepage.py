import streamlit as st
import time

st.set_page_config(
    page_title='Home Page',
    initial_sidebar_state='expanded',
    layout='wide'
)

hide_menu = """
    <style>                               
        #MainMenu {visibility: hidden;}
                
        .reportview-container footer {visibility: hidden;} 

        #footer {
            background-color: Darkorange;
            color: white;
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 2.5rem;
        }
    </style>
    <body>
        <footer id="footer">
            <p><i>Updated 11/07/2022</i></p>
        </footer>
    </body>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.subheader("Eddie Cheung's Python Learning Project")
st.info('##### \N{clipboard} On the left sidebar contains a list of apps written in Streamlit Python')
