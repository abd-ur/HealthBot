import streamlit as st
import subprocess
USERS = {
    'alice': 'password123',
    'bob': 'pass123',
    'charlie': 'password'}
st.write('Please log in')
us=st.text_input('Username')
pas=st.text_input('Password',type='password')
if st.button('Log in'):
    if us in USERS and pas==USERS[us]:
        st.title('MyApp')
        if st.button('Say hello'):
            st.write('Get lost')
        else:
            st.write('Win it all')
        title=st.text_input('Movie title', 'Life of Brian')
        st.write('The current movie title is', title)
    else:
         st.error('Invalid credentials')
