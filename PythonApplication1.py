import pandas as p
import numpy as n
import streamlit as st
st.title('MyApp')
if st.button('Say hello'):
    st.write('Get lost')
else:
    st.write('Win it all')
title=st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
