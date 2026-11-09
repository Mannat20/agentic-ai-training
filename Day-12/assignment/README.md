# Day 12 Assignment - User Registration with File and MongoDB Storage

## 🎯 Objective

The objective of this assignment was to build a user registration flow that takes user details, protects the password, and stores the record in a file and in a MongoDB database.

---

# 📝 Problem Statement

Create a Python program that:

- Takes the name, phone, email and password of a user.
- Does not store the password as plain text.
- Can save the user as a line in a CSV file.
- Can save the user as a document in a MongoDB collection.

---

# 💡 Approach

- The `user` class in `user.py` collects the input and hashes the password using SHA-256.
- `to_csv()` returns the user as a comma-separated string.
- `to_dictionary()` returns the user as a dictionary using `vars()`.
- `fileHelper` appends the CSV string to `users.csv`.
- `DBHelper` connects to MongoDB Atlas and inserts the dictionary into the `users` collection of the `Agentic_AI` database.
- `implement.py` runs the whole flow.

---

# 🧠 Concepts Applied

- Classes and Constructors with Default Arguments
- Password Hashing (`hashlib`, SHA-256)
- Object to CSV and Dictionary Conversion
- File Handling (Append Mode)
- MongoDB Atlas and `pymongo`
- Helper Classes (Separation of Concerns)

---

# 📂 Logic

```
Create user object

Take input from keyboard

Hash the password

Convert user to CSV string     -> append to users.csv
Convert user to dictionary     -> insert into MongoDB

Show confirmation
```

---

# 📷 Output

(Add Program Output Screenshot)

(Add MongoDB Atlas Collection Screenshot)

---

# 📚 Learning Outcome

Through this assignment, I learned:

- How user data moves from the keyboard to a file and a database.
- Why passwords are hashed before storage.
- How a Python dictionary becomes a MongoDB document.
- How helper classes keep the main program clean and reusable.

---

# 🚀 Skills Practiced

- Object-Oriented Programming
- Database Connectivity
- Data Security Basics
- File Handling
- Problem Solving

---

# 📌 Conclusion

This assignment connected object-oriented programming with persistent storage. By saving the same user object to a file and to a cloud database, it showed the difference between simple file storage and a real database, and why sensitive data such as passwords must be protected.
