import streamlit as st
import time
emp=st.empty()
while(1):
  st.title('Login')
  USERS = {
            'alice': 'password123',
            'bob': 'pass123',
            'charlie': 'password'}
  emp.write('Please log in')
  us=emp.text_input('Username')
  pas=emp.text_input('Password',type='password')
  if emp.button('Log in'):
      if us in USERS and pas==USERS[us]:
        st.write('new')
   
        break
      else:
          st.error('Invalid credentials, try again.')
