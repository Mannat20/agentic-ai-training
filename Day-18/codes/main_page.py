import streamlit as st
st.title('Agentic UI Demo')

home_page=st.Page('home_page.py',title='Home Page',icon='🏠')
chat_page=st.Page('chat_page.py',title='Chat Page')
patient_page=st.Page('patient_page.py',title='patient Page')

pg=st.navigation([home_page,chat_page,patient_page])
pg.run()