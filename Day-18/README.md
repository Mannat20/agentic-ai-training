# Day 18 - Regular Expressions and a Multi-Page Agentic AI Dashboard

**Training Program:** Agentic AI Training

**Organization:** Auribises

**Day:** 18

---

# 📖 Session Overview

The eighteenth day had two parts.

The first part introduced **Regular Expressions (Regex)** using Python's `re` module, which makes it easy to search, extract and validate patterns in text such as phone numbers, emails, PAN numbers and vehicle registration numbers.

The second part continued the Agentic AI application. A **multi-page Streamlit app** was created with a dashboard, an AI chat page and a patients page, and the AI task manager (OpenAI Function Calling with MongoDB) was placed inside it.

---

# 📚 Topics Covered

## Regular Expressions

- `re.search()`
- `re.findall()`
- `re.fullmatch()`
- Raw Strings (`r"..."`)
- Character Classes and Quantifiers (`\d`, `\S`, `+`, `{n}`, `[A-Z]`)
- Alternation using `|`

---

## Extraction and Validation

- Extracting Numbers, Emails, Phone Numbers and Vehicle Numbers
- Validating a 10-digit Phone Number
- Validating a PAN Number
- Validating a Vehicle Registration Number
- Combining Several Patterns in One Expression

---

## Multi-Page Streamlit App

- `st.Page()` and `st.navigation()`
- Home Page with `st.metric()`, `st.columns()`, `st.line_chart()`, `st.dataframe()`
- Patients Page
- AI Chat Page

---

## AI Task Manager

- OpenAI Function Calling with Four Tools
- MongoDB through `DBHelper`
- `@st.cache_resource`, Session State and Typing Effect

---

# 🎯 Learning Outcomes

By the end of this session, I learned:

- How to write patterns to find and validate text.
- The difference between `search`, `findall` and `fullmatch`.
- How to validate real-world formats such as PAN and vehicle numbers.
- How to build a Streamlit app with several pages and a navigation menu.
- How to show metrics, charts and tables in a dashboard.
- How the AI chat page fits into a bigger application.

---

# 📂 Folder Structure

```
Day-18
│
├── README.md
├── Notes.md
├── code/                      # add your Day-18 code files here
├── assignment/
│   └── README.md
└── images/
    ├── day18-regex-basics.png
    ├── day18-regex-validation.png
    ├── day18-streamlit-dashboard.png
    ├── day18-agentic-chat.png
    ├── day18-function-calling.png
    ├── day18-mongodb-integration.png
    └── day18-final-application.png
```

---

# 🛠️ Technologies Used

- Python 3 (`re` module)
- Streamlit
- pandas
- OpenAI API
- MongoDB Atlas and `pymongo`
- Visual Studio Code
- Git
- GitHub

---

# 📌 Key Takeaways

- `fullmatch` validates the **whole** input, while `search` finds a pattern anywhere.
- Always write patterns as raw strings.
- `st.navigation()` turns separate Python files into pages of one app.
- A good project separates pages, database code and AI logic.

---
