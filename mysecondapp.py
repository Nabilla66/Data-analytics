import streamlit as st
import pandas as pd

st.header("My Second Streamlit App")

st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')
if show:
    st.write(pd.DataFrame({
    'Cell.size': [1, 4, 1, 1, 3, 7, 4, 3, 1, 1],
    'Class': [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
}))
