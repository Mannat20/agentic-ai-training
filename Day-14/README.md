# Day 14 - Chat-Based Task Manager using Streamlit and MongoDB

**Training Program:** Agentic AI Training

**Organization:** Auribises

**Day:** 14

---

# 📖 Session Overview

The fourteenth day combined everything from the previous sessions into one application: a chat interface where tasks can be created, listed, updated and deleted by typing commands.

The session introduced Streamlit's chat components and session state, added a delete operation to `DBHelper`, and used simple text parsing to turn a typed message into a database action. This is the first step towards an agent that understands a request and acts on it.

---

# 📚 Topics Covered

## Streamlit Chat Interface

- Page Setup using `st.set_page_config()`
- `st.chat_input()` for User Messages
- `st.chat_message()` for Chat Bubbles
- `st.markdown()` for Displaying Text
- Typing Effect using `st.empty()` and `time.sleep()`

---

## Session State

- Why Streamlit Needs `st.session_state`
- Storing the Chat History
- Re-displaying Previous Messages

---

## Command Parsing

- Splitting a Command using `split(':')` and `split(',')`
- Matching Keywords inside a Message
- Help Messages using a Dictionary of Clues

---

## CRUD with MongoDB

- **Create** using `insert_one()`
- **Read** using `find()`
- **Update** using `update_one()` with `$set`
- **Delete** using `delete_one()`
- Using `deleted_count` to Check the Result

---

## Other

- Adding a Timestamp using `datetime`
- Task Status Field
- Formatting a Document using `format_map()`

---

# 🎯 Learning Outcomes

By the end of this session, I learned:

- Building a chat-style user interface in Python.
- Keeping chat history alive across Streamlit re-runs.
- Turning a typed sentence into structured data.
- Implementing all four CRUD operations on a MongoDB collection.
- Giving the user clear feedback after every action.
- Structuring a larger program using a helper class.

---

# 📂 Folder Structure

```
Day-14
│
├── README.md
├── Notes.md
├── code/
│   ├── chat_bot.py
│   └── db_Helper.py
├── assignment/
│   └── README.md
└── images/
```

---

# 🛠️ Technologies Used

- Python 3
- Streamlit
- MongoDB Atlas
- `pymongo`
- Visual Studio Code
- Git
- GitHub

---

# 📌 Key Takeaways

- Streamlit re-runs the script on every interaction, so chat history must be saved in session state.
- CRUD (Create, Read, Update, Delete) is the base of almost every application.
- Helper classes keep the database code out of the user interface code.
- Text-command parsing is a simple beginning for an AI agent that acts on user requests.

---
