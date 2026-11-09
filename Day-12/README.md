# Day 12 - User Class, Password Hashing, and Introduction to MongoDB

**Training Program:** Agentic AI Training

**Organization:** Auribises

**Day:** 12

---

# 📖 Session Overview

The twelfth day focused on storing application data permanently, first in a file and then in a database.

A `User` class was designed to collect registration details, protect the password using hashing, and convert the data into CSV and dictionary formats. The session then introduced MongoDB Atlas and the `pymongo` library, and a `DBHelper` class was created to connect to the database and save documents.

---

# 📚 Topics Covered

## User Class

- Constructor with Default Values
- Taking Input from the User
- Displaying Details
- Converting Object to CSV String
- Converting Object to Dictionary using `vars()`

---

## Password Security

- Hashing using `hashlib`
- SHA-256
- One-Way Hashing

---

## File Helper

- Writing Records to a CSV File
- Reusable `fileHelper` Class

---

## MongoDB

- What is MongoDB (NoSQL Document Database)
- MongoDB Atlas (Cloud Database)
- Connection URI
- `pymongo` and `MongoClient`
- Checking the Connection using `ping`
- Database, Collection and Document
- `insert_one()`

---

## DBHelper Class

- Creating a Connection
- Selecting a Collection
- Saving a Document

---

# 🎯 Learning Outcomes

By the end of this session, I learned:

- Designing a class that represents a real entity (a user).
- Why passwords must never be stored as plain text.
- Converting one object into different formats (CSV and dictionary).
- Separating storage logic into helper classes.
- Connecting a Python program to a cloud MongoDB database.
- How data is organised in MongoDB as databases, collections and documents.

---

# 📂 Folder Structure

```
Day-12
│
├── README.md
├── Notes.md
├── code/
│   ├── user.py
│   ├── fileHelper.py
│   ├── dbHelper.py
│   ├── implement.py
│   ├── mongo.py
│   ├── db.py
│   └── users.csv
├── assignment/
│   └── README.md
└── images/
```

---

# 🛠️ Technologies Used

- Python 3
- `hashlib`
- MongoDB Atlas
- `pymongo`
- Visual Studio Code
- Git
- GitHub

---

# 📌 Key Takeaways

- A helper class keeps storage code separate from the main program.
- A hash cannot be converted back to the original password.
- A Python dictionary maps directly to a MongoDB document.
- Database credentials must never be committed to GitHub.

---
