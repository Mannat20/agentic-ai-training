# Day 14 Notes

---

# Project Idea - Delegate a Task through Chat

The user types a task in a chat box. The program understands the command, saves or changes the task in MongoDB, and replies in the chat.

```
User types command
        |
Chat bot checks the message
        |
   +----+--------+---------+---------+
   v             v         v         v
 create         list     update    delete
   |             |         |         |
        MongoDB  (collection: task)
        |
Reply shown in chat
```

### Commands Supported

| Command | Format |
|---------|--------|
| Create | `create task: title, description, action, contact_name, contact_phone` |
| List | any message containing `list`, e.g. `list all tasks` |
| Update | `update task: title, description, action, contact_name, contact_phone` |
| Delete | `delete task: title` |

Example

```
create task: Call Plumber, fix the kitchen tap, call, Ramesh, 9876543210
```

---

# Streamlit Chat Components

```python
import streamlit as st

st.set_page_config('Agentic Chat UI')
st.subheader('Write a Task to Delegate')
```

| Function | Purpose |
|----------|---------|
| `st.set_page_config()` | Sets the browser tab title |
| `st.subheader()` | Shows a heading |
| `st.chat_input()` | Chat box at the bottom of the page; returns the typed text |
| `st.chat_message(role)` | Creates a chat bubble for `'user'` or `'assistant'` |
| `st.markdown()` | Writes text inside the bubble |

---

# Session State

Streamlit **re-runs the whole script** every time the user sends a message, so normal variables are reset. To keep the chat history, it is stored in `st.session_state`, which survives re-runs.

```python
if 'messages' not in st.session_state:
    st.session_state.messages = []
```

### Showing Previous Chat

```python
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
```

- Every message is a dictionary: `{'role': ..., 'content': ...}`.
- The loop redraws the old messages on every re-run.

### Saving a New Message

```python
message = {'role': 'user', 'content': user_input}
st.session_state.messages.append(message)
```

(Add Chat UI Screenshot)

---

# Typing Effect

The reply appears character by character, like a person typing.

```python
with st.chat_message('assistant'):
    typing_placeholder = st.empty()
    typing_text = ''
    for character in message['content']:
        typing_text += character
        typing_placeholder.markdown(typing_text)
        time.sleep(0.02)
```

- `st.empty()` reserves a placeholder that can be overwritten.
- Each loop adds one character and redraws the placeholder.
- `time.sleep(0.02)` gives a short pause between characters.

The same block is repeated for every reply, so it is a good candidate for a function.

---

# Help Messages (task_clues)

A dictionary maps a question to the command format.

```python
task_clues = {
    'how to create a task': 'create task: title, description, action(call etc), contact_name, contact_phone',
    'how to view tasks': 'list all tasks',
    'how to update task': 'update task: title, description, action(call etc), contact_name, contact_phone',
    'how to delete task': 'delete task: title',
}

if user_input in task_clues:
    clue = task_clues[user_input]
```

- If the message exactly matches a key, the bot replies with the matching clue.

---

# Parsing a Command

```python
data1 = user_input.split(':')
data2 = data1[1].split(',')
```

For `create task: Call Plumber, fix tap, call, Ramesh, 9876543210`

| Step | Result |
|------|--------|
| `split(':')` | `['create task', ' Call Plumber, fix tap, call, Ramesh, 9876543210']` |
| `data1[1].split(',')` | `[' Call Plumber', ' fix tap', ' call', ' Ramesh', ' 9876543210']` |
| `.strip()` on each | Removes the extra spaces |

---

# CRUD Operations

## Create

```python
task = {
    'title': data2[0].strip(),
    'description': data2[1].strip(),
    'action': data2[2].strip(),
    'contact_name': data2[3].strip(),
    'contact_phone': data2[4].strip(),
    'status': 'pending',
    'time': datetime.datetime.now()
}
db_helper.save_document(task)
```

- `status` starts as `'pending'`.
- `time` stores when the task was created.

## Read

```python
document = db_helper.retrieve()

tasks = ''
for doc in document:
    tasks += dict_to_string(doc)
```

`dict_to_string()` uses `format_map()` (from Day 10) to turn a document into a readable line.

```python
def dict_to_string(task):
    return ('Title: {title},description: {description},action: {action},'
            'contact_name: {contact_name},contact_phone: {contact_phone}').format_map(task)
```

## Update

```python
title = data2[0].strip()
condition = {'title': title}
updated_data = { ...new values... }
db_helper.update(condition, updated_data)
```

- The task is found by its **title**.
- `$set` (inside `DBHelper.update`) changes only the given fields.

## Delete

```python
title = data1[1].strip()
condition = {'title': title}
deleted_count = db_helper.delete_document(condition)

if deleted_count and deleted_count > 0:
    content = 'Deleted Successfully.'
else:
    content = 'Document was not found.'
```

- `delete_one()` removes the first matching document.
- `deleted_count` tells whether anything was actually deleted, so the bot can give the correct reply.

## Anything Else

```python
'Sorry, request not served.'
```

---

# DBHelper (Updated)

| Method | MongoDB Call | Added On |
|--------|--------------|----------|
| `select_collection()` | `db[collection]` | Day 12 |
| `save_document()` | `insert_one()` | Day 12 |
| `retrieve()` | `find()` | Day 13 |
| `update()` | `update_one()` with `$set` | Day 13 |
| `delete_document()` | `delete_one()` | **Day 14** |

New in `delete_document()`

```python
def delete_document(self, condition):
    id = self.collection.delete_one(condition)
    print('[DBHelper] Delete_count.', id.deleted_count)
    return id.deleted_count
```

`retrieve()` now also **returns** the cursor, so the chat bot can use the documents.

The chat bot selects the collection named `task`:

```python
db_helper = DBHelper()
db_helper.select_collection('task')
```

---

# CRUD Summary

| Operation | Chat Command | MongoDB Method |
|-----------|--------------|----------------|
| Create | `create task: ...` | `insert_one()` |
| Read | `list all tasks` | `find()` |
| Update | `update task: ...` | `update_one()` |
| Delete | `delete task: title` | `delete_one()` |

(Add Create / List / Update / Delete Screenshots)

---

# Things to Revisit

- **Listing shows nothing.** `retrieve()` loops over the cursor to print the documents, and then returns the same cursor. A MongoDB cursor can be read only once, so by the time `chat_bot.py` loops over it, it is already used up. Converting the result to a list inside `retrieve()` (`list(result)`) avoids this.
- Messages are matched by keywords such as `'list'`, `'update'` and `'delete'` anywhere in the text, so an unrelated sentence containing one of these words triggers that command.
- The reply for **create** is displayed but not added to `st.session_state.messages`, so it disappears on the next re-run.
- The commands break if the user types fewer than five comma-separated values, because the code indexes `data2[4]` directly.
- The database password is written directly in `db_Helper.py`; it should be moved out of the code.

---

# Summary

Today's session focused on building a chat-based task manager that connects a Streamlit interface to MongoDB and supports create, list, update and delete operations through typed commands.
