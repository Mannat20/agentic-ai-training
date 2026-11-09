# Day 20 - Delegate AI: Project Foundation and Contact Management

**Training Program:** Agentic AI Training

**Organization:** Auribises

**Day:** 20

---

# 📖 Session Overview

The twentieth day marked the start of the capstone project, **Delegate AI**.

Instead of learning one concept at a time, the project combines everything learned so far into one application. This session built the foundation: the project directory was organized into modules, all external services were configured through environment variables, a reusable MongoDB helper class was written, and a list of contacts was imported from a JSON file into MongoDB Atlas. These contacts will be used later when the AI agent makes calls.

---

# 📚 Topics Covered

## Project Structure

- Splitting the Application into Several Python Modules
- Separate Files for Configuration, Database, AI, Contacts and Calling
- Installing the Required Dependencies

---

## Configuration

- Environment Variables
- `python-dotenv` and `load_dotenv()`
- `os.getenv()`
- Creating the OpenAI, ElevenLabs and MongoDB Clients in One Place

---

## Database Initialization

- `DBHelper` Class (Reusable)
- Collections `tasks` and `contacts`
- `save()`, `save_many()`, `retrieve()`, `update()`, `delete()`

---

## Contact Management

- Contacts Stored in a JSON File
- Reading and Parsing the File with `json.loads()`
- Importing Many Documents using `insert_many()`

---

# 🎯 Learning Outcomes

By the end of this session, I learned:

- How a real Python project is organized into modules.
- Why configuration must be separate from application logic.
- How to keep API keys and passwords out of the source code.
- How to design a reusable database helper.
- How to load initial data from a JSON file into MongoDB.

---

# 📂 Folder Structure

```
Day-20
│
├── README.md
├── Notes.md
├── code/                      # add your Delegate AI project files here
├── assignment/
│   └── README.md
└── images/
    ├── day20-project-directory.png
    ├── day20-config-file.png
    ├── day20-database-helper.png
    └── day20-contacts-import.png
```

---

# 🛠️ Technologies Used

- Python 3
- `python-dotenv`
- OpenAI API
- ElevenLabs
- MongoDB Atlas and `pymongo`
- JSON
- Visual Studio Code
- Git
- GitHub

---

# 📌 Key Takeaways

- A modular structure makes a project easier to maintain, debug and extend.
- Secrets belong in a `.env` file, which must be listed in `.gitignore`.
- A single configuration module gives every other file the same clients.
- JSON files are a simple way to load initial data.

---
