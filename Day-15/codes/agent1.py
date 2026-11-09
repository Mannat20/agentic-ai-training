
from db_Helper import DBHelper
from openai import OpenAI
import json
import datetime
from config import openai_api_key1
#database initialization
db_helper=DBHelper()
db_helper.select_collection('task')
#openai
openai_api_key = openai_api_key1
client = OpenAI(api_key=openai_api_key)

# creating a function (data save in mogoDB)
def save_task(task):
    task['status']='pending',
    task['created_at']=datetime.datetime.now(),
    db_helper.save_document(task)
    print( 'Task saved Successfully ')

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

input_list=[{
    'role':'user','content':"Call gourav on 9872898728 and assign a task to create 3 licenses for finlo for bus ticketing module for Jujhar group"
}]
# Request to LLM
response = client.responses.create(
    model="gpt-4o-mini",
    tools=tools,
    input=input_list,
)
print("Output:")
llm_output = response.model_dump_json(indent=2) # string

llm_output=json.loads(llm_output)
print(llm_output)
# argument=json.loads(llm_output['output'][0]['arguments'])
# function_name=llm_output['output'][0]['name']
# type=llm_output['output'][0]['type']
# print(f'TASK DETAILS: \nArgumnets: {argument}\nfunction_name: {function_name}\ntype: {type}')

# if type=='function_call':
#     if function_name=='save_task':
#         save_task(argument)