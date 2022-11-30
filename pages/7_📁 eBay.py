import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image

st.caption('*Page under construction*')
st.title('My eBay Listings')

showImg = """
    <img src="https://i.ebayimg.com/images/g/m-EAAOSwl1diWZJN/s-l500.jpg" 
     width="60" height="40">
"""
st.markdown(showImg, unsafe_use_html=True)
st.write('---')
st.image('https://i.ebayimg.com/images/g/m-EAAOSwl1diWZJN/s-l500.jpg')

