import streamlit as st
import random
st.title("Hi I am LIFE, your personal health care assistant. You can start chatting.")
rules={
    "hi": ["Hello", "Hi"],
    "bye": ["Goodbye, Take care", "Bye!"],
    "default": ["Sorry, I could'nt understand."]}
def match(inp):
    res=rules.get(inp.lower(),rules["default"])
    return random.choice(res)
inp=st.text_input("You:","")
if st.button("Send"):
    res=match(inp)
    st.text_area("Bot:",res)
