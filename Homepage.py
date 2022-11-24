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
        footer {
            visibility: hidden;
        }
        footer:after {
            visibility: visible;
            content: 'Updated 11/17/2022';
            font-style: italic;
            display: block;    
            text-align: center;
            background: white;
            color: black;
            padding: 5px;
            height: 35px;
        }   
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.write("#### Eddie Cheung's Python Learning Project")
st.markdown("""---""")
st.info('##### \N{clipboard} Sidebar menu contains a list of apps written in Streamlit Python')
st.success("###### [Feel free to check out my bio](https://my.indeed.com/p/chichiueddiec-5mgjx37) and [drop me some feedbacks or ideas](https://chicheung.streamlit.app/Feedback_Form)")
