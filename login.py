import streamlit as st
import random
st.title("Hi I am LIFE, your personal health care assistant. You can start chatting.")
rules={
    "hi": ["Hello", "Hi"],
    'checkup':['Shall we start your diabetes diagnosis?','Ok then, we will begin your diagnosis then.']
    'diabetes':['Shall we start your diabetes diagnosis?','Ok then, we will begin your diagnosis then.']
    'sugar':['Would you like to go for a quick diagnosis?']
    'no':['Ok we will take it on someother time.]
    "bye": ["Goodbye, Take care", "Bye!"],
    "default": ["Sorry, I could'nt understand."]}
def match(inp):
    for key in rules:
        if key in inp:
          return random.choice(rules[key])
inp=st.text_input("You:","")
if st.button("Send"):
    res=match(inp)
    st.text_area("Bot:",res)
