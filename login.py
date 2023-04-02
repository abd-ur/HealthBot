import streamlit as st

# Define the options for the selectbox
options = ["Home", "Page 1", "Page 2"]

# Create a sidebar with the selectbox
selection = st.sidebar.selectbox("Go to", options)

# Show the appropriate content based on the selected option
if selection == "Home":
    st.write("This is the home page.")
elif selection == "Page 1":
    st.write("This is page 1.")
elif selection == "Page 2":
    st.write("This is page 2.")
