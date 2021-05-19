import streamlit as st
from PIL import Image

def app():
    st.subheader("""Maths is important
    """)
    image = Image.open('Homer.jpg')
    st.image(image)
    