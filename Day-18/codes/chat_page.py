import streamlit as st
import time
from openai import OpenAI
from db_Helper import DBHelper
import datetime
import json
st.set_page_config('Agentic Chat UI')
st.subheader('Write a Task to Delegate')

db_helper=DBHelper()
db_helper.select_collection('task')

openai_api_key = ''
client = OpenAI(api_key=openai_api_key)

def save_task(task):
    task['status']='pending',
    task['created_at']=datetime.datetime.now(),
    db_helper.save_document(task)
    print( 'Task saved Successfully ')

# def update_task(condition,updated_data):
#     db_helper.update(condition,updated_data)
#     print( 'Task updated Successfully ')
# 2. tool

tools = [
    {
        "type": "function",
        "name": "save_task",
        "description": "Save the task in MongoDB Atlas",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Title of the Task",
                },
                "description": {
                    "type": "string",
                    "description": "Description of the Task",
                },
                "action": {
                    "type": "string",
                    "description": "Action of the Task can be call, message or email",
                },
                "contact_name": {
                    "type": "string",
                    "description": "Name of the contact person who will perfrom this Task",
                },
                "contact_phone": {
                    "type": "string",
                    "description": "Phone of the person who will perfrom this Task",
                }
            },
            "required": ["title", "description", "action", "contact_name", "contact_phone"],
        },
    },
]

if 'messages' not in st.session_state:
    st.session_state.messages=[]

# Used loop for showing the previous chats too
for message in st.session_state.messages:
     with st.chat_message(message['role']):
            st.markdown(message['content'])

user_input=st.chat_input('Enter your task here.')
if user_input:
    message={
        'role':'user',
        'content':user_input
    }
    with st.chat_message(message['role']):
        st.markdown(message['content'])
    st.session_state.messages.append(message)

input_list=[{
    'role':'user','content':user_input
}]

response = client.responses.create(
    model="gpt-4o-mini",
    tools=tools,
    input=input_list,
)

print("Output:")
llm_output = response.model_dump_json(indent=2) # string
llm_output=json.loads(llm_output)

argument=json.loads(llm_output['output'][0]['arguments'])
function_name=llm_output['output'][0]['name']
type=llm_output['output'][0]['type']
result='Sorry ! request was not served.'
if type=='function_call':
    if function_name=='save_task':
        result=save_task(argument)
    elif function_name=='update_task':
         pass
    elif function_name=='delete_task':
         pass
    elif function_name=='list_task':
         pass
    
    message={
         'role':'assistant',
         'content':result
    }
    st.session_state.messages.append(message)
    with st.chat_message(message['role']):
        typing_placeholder=st.empty()
        typing_text=''
        for character in message['content']:
            typing_text+=character
            typing_placeholder.markdown(typing_text)
            time.sleep(0.02)