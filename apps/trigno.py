import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd

def app():
    options = ["Sin", "Cos",  "Tan"]
    choice = st.radio("Choose the Operation", options)
    if choice == "Sin":

        multi_sin = ["simple Sin" , "arc Sin" , "hyperbolic Sin"]
        choices = st.radio("Choose the appropriate sin function", multi_sin)
        st.write("sins")
        if choices == "simple Sin":
            a = st.number_input("Please Entre Number for sin")
            c=math.sin(a)
            st.text("The result of sin is")
            st.write(c)
            image = Image.open('today.jpeg')
            st.image(image)
            st.text("i ate some pie ... ")
        elif choices == "arc Sin":
            a = st.number_input("Please Entre Number for arc sin")
            c=math.asin(a)
            st.text("The result of arc sin is")
            st.write(c)
            image = Image.open('today.jpeg')
            st.image(image)
            st.text("i ate some pie ... ")
        elif choices == "hyperbolic Sin":
            a = st.number_input("Please Entre Number for hyperbolic sin")
            c=math.sinh(a)
            st.text("The result of hyperbolic sin is")
            st.write(c)
            image = Image.open('today.jpeg')
            st.image(image)
            st.text("i ate some pie ... ")


        
    elif choice == "Cos":
        multi_cos = ["simple Cos" , "arc Cos" , "hyperbolic Cos"]
        choices = st.radio("Choose the appropriate sin function", multi_cos)

        if choices == "simple Cos":
            a = st.number_input("Please Entre Number for cos")
            c=math.cos(a)
            st.text("The result of Cos is")
            st.write(c)
            image = Image.open('today.jpeg')
            st.image(image)
            st.text("i ate some pie ... ")

        elif choices == "arc Cos":
            a = st.number_input("Please Entre Number for arc cos")
            c=math.acos(a)
            st.text("The result of arc cos is")
            st.write(c)
            image = Image.open('today.jpeg')
            st.image(image)
            st.text("i ate some pie ... ")
        elif choices == "hyperbolic Cos":
            a = st.number_input("Please Entre Number for hyperbolic Cos")
            c=math.sinh(a)
            st.text("The result of hyperbolic Cos is")
            st.write(c)
            image = Image.open('today.jpeg')
            st.image(image)
            st.text("i ate some pie ... ")
    elif choice == "Tan":
        multi_tan = ["simple Tan" , "arc Tan" , "hyperbolic Tan"]
        choices = st.radio("Choose the appropriate sin function", multi_tan)

        if choices == "simple Tan":
            a = st.number_input("Please Entre Number for Tan")
            c=math.tan(a)
            st.text("The result of Tan is")
            st.write(c)
            image = Image.open('today.jpeg')
            st.image(image)
            st.text("i ate some pie ... ")
        elif choices == "arc Tan":
            a = st.number_input("Please Entre Number for arc Tan")
            c=math.atan(a)
            st.text("The result of arc Tan is")
            st.write(c)
            image = Image.open('today.jpeg')
            st.image(image)
            st.text("i ate some pie ... ")
        elif choices == "hyperbolic Tan":
            a = st.number_input("Please Entre Number for hyperbolic Tan")
            c=math.tanh(a)
            st.text("The result of hyperbolic Cos is")
            st.write(c)
            image = Image.open('today.jpeg')
            st.image(image)
            st.text("i ate some pie ... ")
