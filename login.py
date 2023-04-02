import streamlit as st

def login():
    # Show the login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Verify the login credentials
        if username == "admin" and password == "123":
            # Clear the login form and show the main screen
            username = ""
            password = ""
            st.success("Logged in!")
            main()
        else:
            st.error("Invalid username or password")

def main():
    # Show the main screen
    st.write("Hello, world!")
    if st.button("Logout"):
        # Clear the main screen and show the login form
        st.experimental_set_query_params()
        login()

if __name__ == '__main__':
    # Start with the login form
    login()
