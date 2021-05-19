import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
    options = ["Addition", "Subtraction",  "Division" ,"Multiplication"]
    choice = st.radio("Choose the Operation", options)
    if choice == "Addition":
        image = Image.open('realmath.jpg')
        st.image(image)
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        c = a+b
        st.text("The result of addition is")
        st.write(c)
    elif choice == "Subtraction":
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        c = a - b
        st.text("The result of Subtraction is")
        st.write(c)
    elif choice == "Multiplication":
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        c = a * b
        st.text("The result of Multiplication is")
        st.write(c)
    elif choice == "Division":
        st.warning("Divisor must greater or equal to 1! entre value fix the error promt!")
        
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        image = Image.open('iamu.png')
        st.image(image)
        remainder = a % b
        modulus = a / b
        st.write("Results are : ")
        st.write(" Reminder is ",remainder)
        st.write(" Modulus is ",modulus)
        
