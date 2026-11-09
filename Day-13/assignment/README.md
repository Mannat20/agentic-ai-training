# Day 13 Assignment - Update User Data and Registration Form

## 🎯 Objective

The objective of this assignment was to practise reading and updating MongoDB documents, and to build the first web form with Streamlit.

---

# 📝 Problem Statement

## Part 1 - Update a User

Using the `DBHelper` class,

- Find a user by email.
- Change the email to a new value.
- Retrieve all users to confirm the change.

## Part 2 - User Registration Form

Create a Streamlit page that takes the name, phone, email and password of a user, with the password hidden while typing.

---

# 💡 Approach

## Part 1

- Add `retrieve()` and `update()` methods to `DBHelper`.
- In `session13.py`, create a condition dictionary and an update dictionary.
- Call `update()` and then `retrieve()` to show the result.

## Part 2

- Use `st.title()` for the heading and `st.text_input()` for every field.
- Use `type='password'` for the password field.
- Use `st.button()` to trigger the registration action.

---

# 🧠 Concepts Applied

- MongoDB Queries (`find`)
- MongoDB Update (`update_one`, `$set`)
- Dictionaries as Conditions
- Reusable Helper Classes
- Streamlit Widgets
- Event Handling using Buttons

---

# 📂 Logic

```
Part 1

    Select collection

    Condition   -> email to search
    Update data -> new email

    Update the matching document
    Retrieve all documents


Part 2

    Show title

    Take name, phone, email, password

    If button clicked

        Create user object
        Convert it to dictionary
```

---

# 📷 Output

(Add Update Output Screenshot)

(Add Streamlit Registration Form Screenshot)

---

# 📚 Learning Outcome

Through this assignment, I learned:

- Updating a single field of a stored document.
- Writing database operations once and reusing them.
- Creating an interactive web page using only Python.
- How a button click triggers code in Streamlit.

---

# 🚀 Skills Practiced

- Database Operations
- Web Interface Basics
- Modular Programming
- Debugging
- Python Fundamentals

---

# 📌 Conclusion

This assignment extended the database helper with retrieve and update operations and introduced Streamlit for building a user-facing form. Together they prepare the ground for a complete application where users interact with data through a web page.
