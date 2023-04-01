import streamlit as st
USERS = {
    'alice': 'password123',
    'bob': 'pass123',
    'charlie': 'password'}
st.write('Please log in')
us=st.text_input('Username')
pas=st.text_input('Password',type='password')
if st.button('Log in'):
    if us in USERS and pas==USERS[us]:
        subprocess.Popen(['streamlit', 'run', 'https://mangekkyo-testapp-pythonapplication1-ob04e2.streamlit.app'])
    else:
        st.error('Invalid credentials')
