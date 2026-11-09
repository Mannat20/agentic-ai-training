# Day 19 - ElevenLabs Voice Agent Integration

**Training Program:** Agentic AI Training

**Organization:** Auribises

**Day:** 19

---

# 📖 Session Overview

The nineteenth day made the Agentic AI application more interactive by adding a **voice assistant**.

An ElevenLabs Conversational AI widget was embedded inside the Streamlit app, so a user can talk to the assistant instead of typing. The application was organized into four pages (Home, AI Chat, Patients and Voice Agent) using Streamlit navigation, and a Customer Support page was created to guide users through the Task Delegation System.

This session was also the end of the practice phase. From the next session the training moved to building a complete project.

---

# 📚 Topics Covered

## Multi-Page Application

- `st.Page()` and `st.navigation()` with Four Pages
- Home, AI Chat, Patients and Agent Pages

---

## AI Task Management

- OpenAI Function Calling with MongoDB (continued)
- CRUD through Natural Language

---

## Voice Agent using ElevenLabs

- ElevenLabs Conversational AI
- Agent ID
- Embedding a Third-Party Widget using `streamlit.components.v1.html()`
- Loading the Widget Script

---

## Customer Support Assistant

- A Page that Explains the Task Delegation System
- Help for Creating, Updating, Deleting and Viewing Tasks

---

## Database Integration

- Reusing `DBHelper` for All Task Operations

---

# 🎯 Learning Outcomes

By the end of this session, I learned:

- How to organize a bigger Streamlit project into several pages.
- How a ready-made AI widget can be embedded with HTML components.
- How an ElevenLabs agent is identified and loaded using its Agent ID.
- How voice can be added to an existing AI application with very little code.
- How OpenAI, MongoDB, Streamlit and ElevenLabs work together.

---

# 📂 Folder Structure

```
Day-19
│
├── README.md
├── Notes.md
├── code/                      # add your Day-19 code files here
├── assignment/
│   └── README.md
└── images/
    ├── day19-navigation.png
    ├── day19-agentic-chat.png
    ├── day19-elevenlabs-widget.png
    └── day19-customer-support.png
```

---

# 🛠️ Technologies Used

- Python 3
- Streamlit
- ElevenLabs Conversational AI
- OpenAI API
- MongoDB Atlas and `pymongo`
- Visual Studio Code
- Git
- GitHub

---

# 📌 Key Takeaways

- A voice interface can be added without rewriting the application.
- `components.html()` lets Streamlit show any HTML widget.
- Four technologies (LLM, database, UI and voice) combine into one product.
- From here on, the sessions build a single real project.

---
