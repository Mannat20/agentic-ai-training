# Day 16 - Functional Programming, Generators, and Decorators

**Training Program:** Agentic AI Training

**Organization:** Auribises

**Day:** 16

---

# 📖 Session Overview

The sixteenth day covered advanced Python features used widely in modern backend, data and AI code.

The session started with lambda functions and the higher-order functions `map()`, `filter()` and `reduce()`. It then explained how iterators and generators produce values one at a time, and ended with two kinds of decorators: Python function decorators and the Decorator Design Pattern from object-oriented programming.

---

# 📚 Topics Covered

## Lambda Functions

- Anonymous Functions
- Comparing `def` and `lambda`
- Lambda with Multiple Arguments
- Functions that Return Functions (Discount Generator)

---

## Map, Filter and Reduce

- `map()` to Transform Every Element
- `filter()` to Select Elements
- `reduce()` to Combine into One Value
- Importing `reduce` from `functools`

---

## Iterators and Generators

- `iter()` and `next()`
- `yield` Keyword
- Generator Functions
- Lazy Evaluation and Memory Efficiency

---

## Decorators

- Function Decorators (`@logger`)
- Nested (Wrapper) Functions
- Decorator Design Pattern using Classes (Burger and Meal)

---

# 🎯 Learning Outcomes

By the end of this session, I learned:

- How to write small anonymous functions using `lambda`.
- That functions can be passed around and returned like variables.
- How to process collections without writing explicit loops.
- How `iter()` / `next()` work and what raises `StopIteration`.
- How generators save memory by producing values lazily.
- How to add behaviour to a function without changing its code.
- How the Decorator Design Pattern extends an object by wrapping it.

---

# 📂 Folder Structure

```
Day-16
│
├── README.md
├── Notes.md
├── code/                      # add your Day-16 code files here
├── assignment/
│   └── README.md
└── images/
    ├── day16-lambda-functions.png
    ├── day16-map-filter-reduce.png
    ├── day16-generators.png
    ├── day16-function-decorator.png
    ├── day16-decorator-pattern.png
    └── day16-flight-assignment.png
```

---

# 🛠️ Technologies Used

- Python 3
- `functools`
- Visual Studio Code
- Git
- GitHub

---

# 📌 Key Takeaways

- `lambda` is best for short, one-expression functions.
- `map`, `filter` and `reduce` make data processing shorter and more readable.
- Generators do not build the whole list in memory.
- Decorators add logging, timing or checks around existing functions.
- The Decorator Design Pattern changes an object's behaviour without editing its class.

---
