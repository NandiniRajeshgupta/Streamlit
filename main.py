import streamlit as st
from sklearn.datasets import load_iris

st.write('hello world')
st.write('gm')
st.balloons()
st.write('hii')

data = load_iris(as_frame=True).frame

st.write(data.head())