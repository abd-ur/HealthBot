import streamlit as st
from streamlit.state.session_state import SessionState

# Define a dictionary of user profiles
USER_PROFILES = {
    'alice': {
        'name': 'Alice',
        'age': 28,
        'location': 'New York'
    },
    'bob': {
        'name': 'Bob',
        'age': 35,
        'location': 'San Francisco'
    }
}

def login():
    # Display a login form to the user
    st.write('Please log in')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Log in'):
        # Check if the username and password are valid
        if username in USER_PROFILES and password == 'password':
            # Set the session state to indicate that the user is logged in
            SessionState.logged_in = True
            # Store the user's profile in the session state
            SessionState.user_profile = USER_PROFILES[username]
        else:
            st.error('Invalid username or password')

def main():
    # Check if the user is logged in
    if not hasattr(SessionState, 'logged_in') or not SessionState.logged_in:
        login()
    else:
        # Display the user's profile
        st.write(f"Name: {SessionState.user_profile['name']}")
        st.write(f"Age: {SessionState.user_profile['age']}")
        st.write(f"Location: {SessionState.user_profile['location']}")

if __name__ == '__main__':
    main()
