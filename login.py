import streamlit as st
import random
import time
ph=st.empty()
st.title("Hi I am LIFE, your personal health care assistant. You can start chatting.")
rules={
    "hi": ["Hello", "Hi"],
    'checkup':['Shall we start your diabetes diagnosis?','Ok then, we will begin your diagnosis then.'],
    'diabetes':['Shall we start your diabetes diagnosis?','Ok then, we will begin your diagnosis then.'],
    'sugar':['Would you like to go for a quick diagnosis?'],
    'yes':['Alright then we will proceed'],
    'no':['Ok we will take it on someother time.'],
    "bye": ["Goodbye, Take care", "Bye!"],
    "default": ["Sorry, I could'nt understand."]}          
def match(inp):
    for key in rules:
        if key in inp:
          return random.choice(rules[key])
def check():
      age=st.number_input("Enter your Age",min_value=0,max_value=150)
      gen=st.radio("Select your Gender",["Male","Female"])
      bmi=st.number_input("Enter your Body Mass Index",min_value=9,max_value=50)
      ins=st.number_input("Enter your recently diagnosed Insulin Level",max_value=300)
      glu=st.number_input("Enter your recently diagnosed Glucose Level",min_value=60,max_value=200)
      bp=st.number_input("Enter your Upper Blood Pressure",min_value=50,max_value=220)
      if st.button('Submit'):
              st.success('Your records are saved.')
              st.write('Age :',age)
              st.write('Gender :',gen)
              st.write('Body Mass Index :',bmi)
              st.write('Insulin level :',ins)
              st.write('Glucose level :',glu)
              st.write('Blood Pressure :',bp)
              import pandas as p
              data=pe.read_csv('https://github.com/mangekkyo/testApp/blob/a17972b2b67523da85349f3accb667db7c36c331/diabetes.csv')
              data=data.drop('Pregnancies',axis='columns')
              data=data.drop('DiabetesPedigreeFunction',axis='columns')
              data=data.drop('SkinThickness',axis='columns')
              from sklearn import linear_model
              mod=linear_model.LinearRegression()
              mod.fit(data.drop('Outcome',axis='columns'),data['Outcome'])
              st.write(round(mod.predict([[89,60,95,28.3,20]])[0]))
      time.sleep(30)
inp=st.text_input("You:","")
if st.button("Send"):
    res=match(inp)
    st.text_area("LIFE:",res)
    if res=='Alright then we will proceed':
       check()
    

   
                    
