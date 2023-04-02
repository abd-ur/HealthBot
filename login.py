import streamlit as st
import time
usr=''
ph=st.empty()
rules={
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "bye": ["Goodbye!", "Bye!", "See you later!"],
    "default": ["I'm sorry, I didn't understand.", "Can you please rephrase that?", "Could you say that again?"]
}
records={'alice':None,'bob':None}
USERS = {
                  'alice': 'password123',
                  'bob': 'pass123',
                  'charlie': 'password'}
with ph.container():
          st.title('Login')
        
          st.write('Please log in')
          us=st.text_input('Username')
          pas=st.text_input('Password',type='password')
          if st.button('Log in'):
              if us in USERS and pas==USERS[us]:
                  st.success('Logging in')
                  time.sleep(3)
                  ph.empty()
                  st.title("Hi I am LIFE, your personal healthcare assistant. You can start chatting.")
                  inp=st.text_input("You:","")
                  if st.button("Send"):
                    res=rules(inp)
                    st.text_area("Life:",res)
                  

                  
                  
              else:
                  st.error('Invalid credentials, try again.')

  
