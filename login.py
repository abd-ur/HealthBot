import streamlit as st
ph=st.empty()
while(1):
    with ph.container():
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
                ph.empty()
                break
            else:
                st.error('Invalid credentials')
            
st.write('welcome')            
