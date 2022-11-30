import streamlit as st
import pandas as pd

st.write("This program divide 2nd number from first")
num1 = st.number_input("1st Number")
num2 = st.number_input("2nd Number")
ans = num1 / num2
st.write('Result is')
st.write(ans)
