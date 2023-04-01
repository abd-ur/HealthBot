USERS = {
    'alice': 'password123',
    'bob': 'pass123',
    'charlie': 'password'}
st.write('Please log in')
us=st.text_input('Username')
pas=st.text_input('Password',type='password')
if st.button('Log in'):
    if us in USERSand pas==USERS[us]:
        st.success('Logged in as {}'.format(us))
    else:
        st.error('Invalid credentials')
