# Day 13 Notes

---

# Recap - DBHelper

`DBHelper` (from Day 12) already supports

- Connecting to the database
- Selecting a collection
- Saving a document with `insert_one()`

Today two more operations were added to the same class: **retrieve** and **update**.

---

# Retrieve Documents

```python
def retrieve(self, condition=None):
    result = self.collection.find(condition)
    for document in result:
        print(document)
```

- `find(condition)` returns a **cursor** over all documents that match the condition.
- If no condition is given, `find(None)` matches **all** documents in the collection.
- The loop prints every matching document.

### Condition (Query Document)

A condition is a dictionary of field and value pairs.

```python
condition = {
    'email': 'mannat@gmail.com'
}
```

| Call | Returns |
|------|---------|
| `retrieve()` | All documents |
| `retrieve({'email': 'mannat@gmail.com'})` | Only documents with that email |

(Add Retrieve Output Screenshot)

---

# Update a Document

```python
def update(self, condition=None, update_data=None):
    result = self.collection.update_one(
        condition,
        {'$set': update_data}
    )
    print('[DBHelper] updated', result)
```

### Parameters

- `condition` selects **which document** to update.
- `update_data` holds the **new values**.

### `update_one()`

- Updates only the **first** document that matches the condition.

### `$set` Operator

- Changes only the fields given in `update_data`.
- All other fields of the document stay as they are.

Without `$set`, the new data would be treated as a replacement, so `$set` is what makes it a partial update.

---

# Using the Update (session13.py)

```python
from dbHelper import DBHelper

def main():
    db = DBHelper()
    db.select_collection()

    condition = {
        'email': 'mannat@gmail.com'
    }
    update_data = {
        'email': 'mannat43@gmail.com'
    }

    db.update(condition, update_data)
    db.retrieve()

if __name__ == '__main__':
    main()
```

### Flow

```
Find document where email = mannat@gmail.com
        |
Set email = mannat43@gmail.com
        |
Retrieve and print all documents to verify
```

- The `users` collection is selected by default.
- `retrieve()` at the end shows the updated data.

(Add Before and After Screenshot)

---

# Streamlit

**Streamlit** is a Python library for building web apps without writing HTML, CSS or JavaScript.

## Installation

```
pip install streamlit
```

## Running an App

```
streamlit run stream.py
```

The app opens in the browser. Streamlit **re-runs the whole script from top to bottom** every time the user interacts with a widget.

---

# User Registration Form (stream.py)

```python
import streamlit as st
from dbHelper import DBHelper

st.title('User Registration')

name = st.text_input('Enter Name')
phone = st.text_input('Enter phone')
email = st.text_input('Enter email')
password = st.text_input('Enter Password', type='password')

if st.button('resgistered'):
    user = User(name, phone, email, password)
    document_to_save = user.to_dictionary()
```

| Streamlit Function | Purpose |
|--------------------|---------|
| `st.title()` | Shows a large page heading |
| `st.text_input()` | Creates a text box and returns what the user typed |
| `type='password'` | Hides the typed characters |
| `st.button()` | Shows a button and returns `True` when it is clicked |

### Idea

1. The form fields return the values typed by the user.
2. When the button is clicked, the values are put into a `User` object.
3. `to_dictionary()` converts the object into a document.
4. The document is then saved using `DBHelper`.

This is the same flow as the console program from Day 12, but with a web form instead of `input()`.

(Add Streamlit Form Screenshot)

---

# Things to Revisit

- `stream.py` uses `User` but never imports it. `from user import user` is needed, and the class is written in lowercase as `user`.
- `document_to_save` is created but not yet passed to `DBHelper.save_document()`, so nothing is stored when the button is clicked.
- `dbHelper.py` in this folder contains the database password written directly in the file. It should be moved to an environment variable before the code is pushed to GitHub.
- `retrieve()` only prints the documents and does not return them; to use the results elsewhere (for example in a web page) the method needs to return the data.

---

# Summary

Today's session focused on reading and updating MongoDB documents using conditions and `$set`, and on creating the first Streamlit web page, a user registration form.
