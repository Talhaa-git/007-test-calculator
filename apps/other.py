import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd

def app():

    options = ["Power" , "Factorial" , "SquareRoot" ]
    choose = st.radio("choose function" , options)
    if choose == "Power":
        a = st.number_input("Entre the number")
        b = st.number_input("to the power")
        c = math.pow(a,b)
        st.write(f"the result, {a} to the power of {b} is ")
        st.write(c)
    elif choose == "Factorial":

        a = st.number_input("entre a positive Integer")
        c = math.factorial(a)
        st.write(f"the result for factorial of {a} is ")
        st.write(c)
    elif choose == "SquareRoot":
        a = st.number_input("entre a Number")
        c = math.sqrt(a)
        st.write(f"the square root of {a} is ")
        st.write(c)
