import streamlit as st

st.set_page_config(
    page_title='Eddie Cheung Home Page',
    page_icon='🏠',
    initial_sidebar_state='auto',
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
            content: 'Updated 11/30/2022';
            font-style: italic;
            display: block;    
            text-align: center;
            background: whitesmoke;
            color: black;
            padding: 5px;
            height: 35px;
        }   
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

ImgUrl = "https://github.com/ChiEddieCheung/Projects/blob/main/abstract.jpg?raw=true"
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("{ImgUrl}");     
             background-size: cover;
             background-repeat: round;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url() 

st.markdown("""
    <style>    
        header.css-18ni7ap.e8zbici2 {
            border: 0px;  
            background-color: lightgray;
        }
        
        span.css-10trblm.e16nr0p30 {
            background-color: yellow;
        }
        
        div.css-zt5igj.e16nr0p33 {
            border: 2px solid black;
        }
    </style>
""", unsafe_allow_html=True)

st.header("Eddie Cheung's Python Learning Project")

st.write('')
st.write('###### \N{clipboard} The sidebar menu contains apps written in Streamlit Python')       

for i in range(5):
    st.write('')

st.write("###### Feel free to check out [My bio]" \
    "(https://my.indeed.com/p/chichiueddiec-5mgjx37) " \
    "and drop me [some feedbacks or ideas]" \
    "(https://chicheung.streamlit.app/Feedback_Form).")
