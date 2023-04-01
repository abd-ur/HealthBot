import streamlit as st
st.write('pass')
if st.button('check'):
    subprocess.Popen(['streamlit', 'run', 'https://mangekkyo-testapp-pythonapplication1-ob04e2.streamlit.app/'])
