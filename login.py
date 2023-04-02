import streamlit as st
def login():   
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
            return us
            break
        else:
            st.error('Invalid credentials, try again.')


# Define the options for the selectbox
options = ["Home", "Login", "Alice",'Bob']

# Create a sidebar with the selectbox
selection = st.sidebar.selectbox("Go to",'Home','Login')

# Show the appropriate content based on the selected option
if selection == "Home":
    st.write("This is the home page.")
elif selection == "Login":
    selection=login()
if selection=='Alice':
  st.write('welcome alice')
elif selection=='Bob':
  st.write('welcome bob')
