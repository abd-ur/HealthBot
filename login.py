import streamlit as st
import time
emp=st.empty()
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
         emp.empty()
         st.write('welcome alice')
         break
      else:
          st.error('Invalid credentials, try again.')
         

