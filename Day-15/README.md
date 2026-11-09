# Day 15 - OpenAI Function Calling and the AI-Powered Agentic Task Assistant

**Training Program:** Agentic AI Training

**Organization:** Auribises

**Day:** 15

---

# 📖 Session Overview

The fifteenth day was a major milestone: the rule-based chat application from Day 14 was turned into an AI-powered assistant.

Instead of checking typed commands with `if` conditions and splitting text, the user's message is now sent to a Large Language Model. The model understands the request in natural language, chooses which Python function should run, and produces the arguments for it. This is called **Function Calling** (also called Tools), and it is the core idea behind agentic AI.

---

# 📚 Topics Covered

## OpenAI Responses API

- Installing and Using the OpenAI Python SDK
- Loading the API Key Safely
- Creating a Client
- `client.responses.create()`
- Model `gpt-4o-mini`
- Reading `response.output_text`

---

## Function Calling (Tools)

- Describing a Python Function to the Model
- Tool Schema in JSON (name, description, parameters, required)
- The Model Choosing the Function and Arguments
- Reading `function_call` from the Response
- Converting JSON Arguments into a Python Dictionary

---

## Agentic Task Assistant

- `save_task()`, `list_tasks()`, `update_task()`, `delete_task()` as Tools
- Optional Fields in `update_task()`
- Complete CRUD through Natural Language
- Streamlit Chat UI with Session State and Typing Effect
- `@st.cache_resource` for the Database Connection

---

## Inspecting the Response

- `type` of Each Output Item (`function_call` or `message`)
- Function Name and Arguments
- Normal Text Reply when No Function is Needed

---

# 🎯 Learning Outcomes

By the end of this session, I learned:

- How to call an LLM from Python using the Responses API.
- How to describe backend functions as tools using JSON schemas.
- How the model decides which function to call and fills in the arguments.
- How to execute the chosen function and show the result in a chat.
- Why separating the AI's decision from the business logic keeps code clean.
- How natural language replaced manual command parsing.

---

# 📂 Folder Structure

```
Day-15
│
├── README.md
├── Notes.md
├── code/                      # add your Day-15 code files here
├── assignment/
│   └── README.md
└── images/
    ├── day15-openai-api.png
    ├── day15-function-calling.png
    ├── day15-tools-schema.png
    ├── day15-agentic-chat.png
    ├── day15-function-execution.png
    ├── day15-crud-tools.png
    └── day15-response-structure.png
```

---

# 🛠️ Technologies Used

- Python 3
- OpenAI API (`openai` SDK, Responses API)
- Streamlit
- MongoDB Atlas and `pymongo`
- Visual Studio Code
- Git
- GitHub

---

# 📌 Key Takeaways

- The LLM decides **what** to do; your Python functions do the actual work.
- A clear tool description and parameter descriptions help the model pick the right tool.
- Arguments come back as a JSON string and must be parsed with `json.loads()`.
- API keys must stay out of source code and out of GitHub.
- This is the foundation of a true agentic application.

---
