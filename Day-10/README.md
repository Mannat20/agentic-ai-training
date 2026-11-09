# Day 10 - Strings, String Formatting, and Toll Plaza Queue

**Training Program:** Agentic AI Training

**Organization:** Auribises

**Day:** 10

---

# 📖 Session Overview

The tenth day focused on working with text data in Python.

The session covered how strings are created and stored, why they are immutable, and how to extract and manipulate parts of a string using indexing and slicing. Different ways of formatting strings were also explored.

The practical part of the day was the Toll Plaza application, which combined classes, object composition, and a circular queue to model vehicles with FastTags passing through a toll booth.

---

# 📚 Topics Covered

## Strings

- Creating Strings (single, double and triple quotes)
- Escape Characters
- Immutability of Strings
- String Methods (`upper()`, `split()`, `strip()` family)
- Membership Check using `in`

---

## Indexing and Slicing

- Positive Indexing
- Negative Indexing
- Slicing
- Reversing a String using `[::-1]`

---

## String Operations

- Concatenation
- Repetition using `*`
- Removing unwanted characters using `rstrip()`

---

## String Formatting

- f-strings
- `format()` with Positional Indexes
- `format_map()` with a Dictionary

---

## Toll Plaza Application

- `FastTag` and `Vehicle` Classes
- Composition (1 Vehicle has 1 FastTag)
- Circular Queue (`TollPlazaQueue`)
- Adding Vehicles to the Queue
- Deducting Toll Tax from FastTag Balance
- Forward and Backward Traversal

---

# 🎯 Learning Outcomes

By the end of this session, I learned:

- How to create and manipulate strings in Python.
- Why strings are immutable and what that means in memory.
- Extracting data from strings using indexing and slicing.
- Splitting text into keywords for simple decision making.
- Formatting output using f-strings, `format()` and `format_map()`.
- Modelling a real-world scenario using multiple classes.
- Implementing a circular queue using `next` and `previous` references.

---

# 📂 Folder Structure

```
Day-10
│
├── README.md
├── Notes.md
├── code/
│   ├── string.py
│   ├── string_formatting.py
│   └── tollPlaza/
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
- Visual Studio Code
- Git
- GitHub

---

# 📌 Key Takeaways

- Strings never change in place; every operation creates a new string.
- Slicing is a powerful tool for extracting parts of structured text such as vehicle registration numbers.
- `format_map()` makes it easy to fill a template from a dictionary.
- Composition lets one object hold another (a Vehicle holds a FastTag).
- A circular queue keeps the last element linked back to the first.

---
