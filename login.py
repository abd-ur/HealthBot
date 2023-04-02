import streamlit as st

def main():
    st.write("Hello, world!")
    if st.button("Clear"):
        # Remove all widgets from the app
        # This also removes the sidebar and header
        # but keeps the footer
        st.experimental_set_query_params()

main()
