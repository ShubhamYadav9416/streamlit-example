import streamlit as st
import pandas as pd

st.write("This program divide 2nd number from first")
num1 = st.number_input("1st Number",min_value=0)
num2 = st.number_input("2nd Number",min_value=1)
ans = num1 / num2
st.write('Result is')
st.write(ans)
