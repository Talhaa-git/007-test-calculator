import streamlit as st
from multiapp import MultiApp
from apps import home, trigno , calculator , Logri , other # import your app modules here

app = MultiApp()

st.markdown("""
#i'm calculator 
""")

st.text("Use Drop Down menu below to navigate between Homepage and Calculator.")

# Add all your application here
app.add_app("Choose Calculations here", home.app)
app.add_app("Basic calculations", calculator.app)
app.add_app("Trignometry", trigno.app)
app.add_app("Logarithms", Logri.app)
app.add_app("Others", other.app)
# The main app
app.run()
