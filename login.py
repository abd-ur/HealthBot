import streamlit as st
while(1):
    st.title('Login')
    USERS = {
            'alice': 'password123',
            'bob': 'pass123',
            'charlie': 'password'}
    st.write('Please log in')
    us=st.text_input('Username')
    pas=st.text_input('Password',type='password')
    if st.button('Log in'):
        if us in USERS and pas==USERS[us]:
            break
        else:
            st.error('Invalid credentials')
       
st.experimental_set_query_params()
st.write('welcome')
