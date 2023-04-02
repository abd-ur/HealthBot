import streamlit as st

def main():
    st.write("Hello, world!")
    if st.button("Clear"):
        empty_container = st.empty()
        empty_container.empty()

main()


