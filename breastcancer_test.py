import pandas as pd
import streamlit as st

breastcancer_test = pd.read_csv("./challenge-breastcancer_test/breastcancer_test.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(breastcancer_test.csv)  # will work for Excel files

st.title("Hi, This is my Third app!")  # add a title
st.write(breastcancer_test)  # visualize my dataframe in the Streamlit app
