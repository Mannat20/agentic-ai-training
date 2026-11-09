# Day 13 - MongoDB Retrieve and Update, and Introduction to Streamlit

**Training Program:** Agentic AI Training

**Organization:** Auribises

**Day:** 13

---

# 📖 Session Overview

The thirteenth day extended the `DBHelper` class with the ability to read and modify data in MongoDB, and introduced Streamlit for building a web interface in pure Python.

The session covered retrieving documents with a condition, updating a document using the `$set` operator, and creating the first Streamlit page, a User Registration form.

---

# 📚 Topics Covered

## MongoDB Operations

- Retrieving Documents using `find()`
- Filtering using a Condition (Query Document)
- Updating a Document using `update_one()`
- `$set` Operator

---

## DBHelper Class (Extended)

- `retrieve()` Method
- `update()` Method
- Reusing the Same Helper across Programs

---

## Streamlit

- What is Streamlit
- Page Title using `st.title()`
- Input Fields using `st.text_input()`
- Password Field using `type='password'`
- Buttons using `st.button()`
- Building a User Registration Form

---

# 🎯 Learning Outcomes

By the end of this session, I learned:

- How to search documents in MongoDB using a condition.
- How to change one field of an existing document without touching the others.
- Passing a condition and new data as dictionaries.
- Creating a simple web form in Python without writing HTML.
- How a button click is used to trigger an action in Streamlit.

---

# 📂 Folder Structure

```
Day-13
│
├── README.md
├── Notes.md
├── code/
│   ├── dbHelper.py
│   ├── session13.py
│   └── stream.py
├── assignment/
│   └── README.md
└── images/
```

---

# 🛠️ Technologies Used

- Python 3
- MongoDB Atlas
- `pymongo`
- Streamlit
- Visual Studio Code
- Git
- GitHub

---

# 📌 Key Takeaways

- A condition is just a dictionary describing which documents to match.
- `$set` changes only the given fields and keeps the rest of the document.
- Streamlit turns a Python script into a web page.
- A web form should reuse the same helper classes as a console program.

---
