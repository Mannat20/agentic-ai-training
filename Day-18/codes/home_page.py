import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
st.title('HOME PAGE')
st.markdown('Welcome to home page.')
# st.write()

st.divider()
col1,col2,col3,col4=st.columns(4)
col1.metric('Patients', 326)
col2.metric('Doctors', 21)
col3.metric('Appointments', 54)
col4.metric('Revenue', '12.5 Lakhs')
st.divider()

left,right=st.columns([2,1])
with left:
    st.subheader('Monthly Patients')
    chart = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Patients': [120, 140, 180, 170, 210, 250]
    })
    st.dataframe(chart,use_container_width=True)
    st.line_chart(
        chart.set_index('Month')
    )
    
with right:
    st.subheader('Departments')

    departments = pd.DataFrame({
        'Department': [
            'Cardiology',
            'Dental',
            'Neuro',
            'Ortho'
        ],
        'Doctors':[5, 4, 7, 8]
    })

    st.dataframe(
        departments,
        use_container_width=True
    )

st.divider()



components.html(
    """
    <elevenlabs-convai agent-id="agent_5901ky1tvv0bfwysz9b8rkb7sw00"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async></script>
    """,
    height=600,
)