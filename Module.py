USERS = {
    'alice': 'password123',
    'bob': 'pass123',
    'charlie': 'password'}
def login():
    st.write('Please log in')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Log in'):
        if username in USERS and password == USERS[username]:
            st.success('Logged in as {}'.format(username))
        else:
            st.error('Invalid username or password')
login()
