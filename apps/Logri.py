import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd

def app():
    st.write("calculating logrithms")
    option = ["Natural log", "base2" , "base10" ,"custom"]

    choose = st.radio("choose appropriate log ", option)
    if choose == "Natural log":
        st.warning("entre positive number to get rid of error msg")
        a = st.number_input("Entre a positive number")
        c = math.log(a)
        st.text("result for natural log is ")
        st.write(c)
    elif choose == "base2":
        st.warning("dont get scare of red thingi :P ")
        a = st.number_input("entre a positive number")
        c = math.log2(a)
        st.text("result for log of base2 is ")
        st.write(c)
    elif choose == "base10":
        st.warning("dont get scare of red thingi :P ")
        a = st.number_input("entre a positive number")
        c = math.log10(a)
        st.text("result for log of base10 is ")
        st.write(c)
    elif choose == "custom":
        st.warning("dont get scare of red thingi :P ")
        a = st.number_input("entre a positive number")
        b = st.number_input("entre base")
        c = math.log(a,b)
        st.write(f"result for log of base '{b}' is ")
        st.write(c)



    
