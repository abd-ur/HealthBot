import streamlit as st
ph=st.empty()
records={'alice':None,'bob':None}
def login():
    with ph.container():
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
            else:
                st.error('Invalid credentials, try again.')
def checkup(x):
  name=st.text_input("Enter your Name")
  age=st.number_input("Enter your Age",min_value=0,max_value=150)
  gen=st.radio("Select your Gender",["Male","Female"])
#  bmi=st.number_input("Enter your Body Mass Index",min_value=9,max_value=50)
#  ins=st.number_input("Enter your recently diagnosed Insulin Level",max_value=300)
#  glu=st.number_input("Enter your recently diagnosed Glucose Level",min_value=60,max_value=200)
#  bp=st.number_input("Enter your Upper Blood Pressure",min_value=50,max_value=220)
  if st.button('Submit'):
    st.success('Your records are saved.')
    x[alice]=age,gen
usr=login()
st.write(usr)
#usr=login() 
#ph.empty()
#st.title('Welcome', usr,'lets check') 
#checkup(records)
#print(records[usr])
