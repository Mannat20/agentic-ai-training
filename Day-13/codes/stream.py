import streamlit as st
from dbHelper import DBHelper
st.title('User Registration')
name=st.text_input('Enter Name')
phone=st.text_input('Enter phone')
email=st.text_input('Enter email')
password=st.text_input('Enter Password',type='password')
if st.button('resgistered'):
    user=User(name,phone,email,password)
    document_to_save=user.to_dictionary()
    