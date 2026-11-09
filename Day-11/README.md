# Day 11 - File Handling, JSON, and Working with APIs

**Training Program:** Agentic AI Training

**Organization:** Auribises

**Day:** 11

---

# 📖 Session Overview

The eleventh day focused on how Python programs read and write data outside the program itself.

The session covered reading and writing text files, converting between Python dictionaries and JSON, and fetching live data from a web API using the `requests` module. The Toll Plaza application from Day 10 was carried forward and used as input for a small file-analysis program.

---

# 📚 Topics Covered

## File Handling

- Opening Files using `open()`
- Reading a File (`read()` and `readlines()`)
- Writing to a File (`'w'` mode)
- Appending to a File (`'a'` mode)
- Closing Files
- `with` Statement

---

## JSON

- What is JSON
- Dictionary to JSON using `json.dumps()`
- JSON to Dictionary using `json.loads()`

---

## Working with APIs

- Calling a REST API using `requests.get()`
- Reading the Response
- Converting the Response to a Dictionary
- Looping through a List of Articles
- Building a News Reader (similar to the Inshorts app)

---

## Object Analysis Program

- Reading a Source File Line by Line
- Counting Mentions of Each Class Name
- Saving the Result in a CSV File

---

## Toll Plaza (Continued)

- `TollPlaza` Folder Carried Forward from Day 10

---

# 🎯 Learning Outcomes

By the end of this session, I learned:

- How to read a file line by line and display its content.
- The difference between write mode and append mode.
- Why files must be closed, and how `with` does it automatically.
- Converting data between Python dictionaries and JSON strings.
- Fetching data from an online API and extracting the required fields.
- Combining file reading and writing in one small program.

---

# 📂 Folder Structure

```
Day-11
│
├── README.md
├── Notes.md
├── code/
│   ├── file_read.py
│   ├── file_write.py
│   ├── file_json.py
│   ├── like_inshot_API.py
│   ├── program.py
│   ├── objectanalysis.csv
│   ├── quotes.txt
│   └── TollPlaza/
│       ├── Vehicle_FastTag.py
│       ├── using_queue.py
│       └── tollPlaza.py
├── assignment/
│   └── README.md
└── images/
```

---

# 🛠️ Technologies Used

- Python 3
- `json` module
- `requests` library
- NewsAPI
- Visual Studio Code
- Git
- GitHub

---

# 📌 Key Takeaways

- Files let a program store data permanently.
- Append mode (`'a'`) keeps old data, while write mode (`'w'`) erases it.
- JSON is the common text format for exchanging data between programs.
- APIs return JSON that can be converted into a dictionary and used directly.
- API keys are secrets and should not be written inside source code.

---
