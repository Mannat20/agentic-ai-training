# Day 14 Assignment - Chat-Based Task Manager

## 🎯 Objective

The objective of this assignment was to build a chat interface that lets a user manage tasks using typed commands, storing every task in MongoDB.

---

# 📝 Problem Statement

Create a Streamlit chat application, "Write a Task to Delegate", that supports:

- **Create** a task with a title, description, action, contact name and contact phone.
- **List** all saved tasks.
- **Update** an existing task using its title.
- **Delete** a task using its title.
- Help messages that explain the command format.
- A polite reply when the request is not understood.

---

# 💡 Approach

- `chat_bot.py` builds the chat interface using `st.chat_input()` and `st.chat_message()`.
- The chat history is stored in `st.session_state.messages` so it stays visible after every re-run.
- Each message is checked: first against the help questions, then for the words `create task`, `list`, `update` and `delete`.
- For create and update, the text after `:` is split by `,` to get the fields.
- `db_Helper.py` contains the `DBHelper` class with save, retrieve, update and delete methods.
- Replies are shown with a typing effect.

---

# 🧠 Concepts Applied

- Streamlit Chat Components
- Session State
- String Parsing (`split`, `strip`)
- Dictionaries
- MongoDB CRUD (`insert_one`, `find`, `update_one`, `delete_one`)
- `datetime` Timestamps
- `format_map()`
- Helper Classes

---

# 📂 Logic

```
Show previous chat messages

Wait for user input

    If input is a help question   -> show the command format

    Else if "create task"         -> split input, save task as pending
    Else if "list"                -> read all tasks and show them
    Else if "update"              -> find task by title, update its fields
    Else if "delete"              -> delete task by title,
                                     reply based on deleted_count
    Else                          -> "Sorry, request not served."
```

---

# 🗂️ Task Document

| Field | Description |
|-------|-------------|
| `title` | Name of the task (used to find it) |
| `description` | What needs to be done |
| `action` | Type of action, e.g. call |
| `contact_name` | Person to contact |
| `contact_phone` | Phone number of the contact |
| `status` | Starts as `pending` |
| `time` | Date and time of creation or update |

---

# 📷 Output

(Add Chat UI Screenshot)

(Add Task Created Screenshot)

(Add MongoDB Atlas `task` Collection Screenshot)

---

# 📚 Learning Outcome

Through this assignment, I learned:

- Creating a chat-style interface in Python.
- Keeping state between interactions in a Streamlit app.
- Turning a typed command into a structured database record.
- Implementing the complete CRUD cycle on a MongoDB collection.
- Giving clear feedback for success and failure.

---

# 🚀 Skills Practiced

- Application Design
- Database Integration
- Input Parsing
- User Interface Development
- Problem Solving

---

# 📌 Conclusion

This assignment brought together classes, file and database handling, and Streamlit into a working task manager. Although the commands are matched by simple keywords, the same structure of understanding a request and acting on it is the foundation for building AI agents that delegate real tasks.
