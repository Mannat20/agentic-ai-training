# 📅 Day 2 – Python Execution Model & Memory Management

## 🎯 Learning Objectives

Today's session focused on understanding Python's internal execution model rather than writing complex programs. We explored how Python executes a program, manages memory, stores objects, and organizes data using different types of containers.

---

# 📚 Topics Covered

- Python Installation
- `__name__` (Dunder Variable)
- Process and Threads
- Stack & Heap Memory
- Model, Container, and Object
- Single Value Container
- Multi Value Container
- Reference Variables
- List
- Tuple

---

# 1. Python Installation

Python was successfully installed and configured on the system. We also learned how to execute Python programs from the terminal.

---

# 2. Dunder Variable (`__name__`)

`__name__` is one of Python's built-in magic (dunder) variables. It helps determine whether a Python file is being executed directly or imported into another Python file.

### 💻 Program

📂 **Source Code:** `code/01_dunder_variable.py`

### 📸 Program Screenshot

*(Insert your code screenshot here)*

### 📸 Output Screenshot

*(Insert terminal output here)*

### 🔍 Observation

- When a file is executed directly, `__name__` becomes `__main__`.
- Python executes statements sequentially from top to bottom.

---

# 3. Process and Threads

Whenever a Python program starts, the Operating System creates a **Process**.

A Process contains:

- Program Code
- Memory
- Resources
- Threads

Every Process contains one **Main Thread**, and additional **Child Threads** can be created if required.

Tasks inside a single thread execute sequentially.

### 📸 Class Diagram

*(Insert Process & Thread diagram here)*

### 🔍 Key Points

- Every Python program runs inside a Process.
- Every Process has one Main Thread.
- Child Threads can also be created.
- Tasks inside one thread execute sequentially.

---

# 4. Stack and Heap Memory

Python mainly uses two memory areas during execution.

## Stack Memory

Stores:

- Reference Variables
- Function Calls

## Heap Memory

Stores:

- Actual Objects
- Values created during execution

### 📸 Memory Diagram

*(Insert Stack & Heap Memory diagram here)*

### 🔍 Observation

Variables never store the actual data.

Instead, they store the **reference (memory address)** of objects stored in Heap Memory.

---

# 5. Model, Container and Object

One interesting concept discussed during today's session was that the terms **Model**, **Container**, and **Object** refer to the same entity but are used in different contexts.

| Term | Context |
|-------|---------|
| Model | Software Architecture |
| Container | Memory Management |
| Object | Programming |

Although the terminology changes, they all represent data stored and managed by Python.

### Types

```
Model / Container / Object
│
├── Single Value Container
│
└── Multi Value Container
```

---

# 6. Single Value Container

A Single Value Container stores only one value.

Python variables are **Reference Variables**, meaning they store the reference (address) of an object instead of the object itself.

The `id()` function returns the identity (memory address) of an object.

When an immutable value changes, Python creates a **new object**, and the reference variable points to the new memory location.

### 💻 Program

📂 **Source Code:** `code/02_single_value_container.py`

### 📸 Program Screenshot

*(Insert screenshot here)*

### 📸 Output Screenshot

*(Insert terminal output here)*

### 🔍 Observation

- Variables store references.
- Objects are stored in Heap Memory.
- Updating immutable data creates a new object.
- Multiple variables with the same immutable value may point to the same object.

---

# 7. Multi Value Container

A Multi Value Container stores multiple values together.

Examples include:

- List
- Tuple

A Multi Value Container may contain:

- **Homogeneous Data** (same data type)
- **Heterogeneous Data** (different data types)

Nested containers are also possible.

### 💻 Program

📂 **Source Code:** `code/03_multi_value_container.py`

### 📸 Program Screenshot

*(Insert screenshot here)*

### 📸 Output Screenshot

*(Insert terminal output here)*

### 🔍 Observation

- Stores multiple values.
- Can be homogeneous or heterogeneous.
- Nested containers are supported.

---

# 8. List

A List is a mutable, ordered collection that allows duplicate values.

### Properties

- Ordered
- Mutable
- Duplicate values allowed

### 💻 Program

📂 **Source Code:** `code/03_multi_value_container.py`

### 📸 Screenshot

*(Insert List example screenshot here)*

### 🔍 Observation

List elements can be modified after creation.

---

# 9. Tuple

A Tuple is an immutable, ordered collection that allows duplicate values.

### Properties

- Ordered
- Immutable
- Duplicate values allowed

### 💻 Program

📂 **Source Code:** `code/03_multi_value_container.py`

### 📸 Screenshot

*(Insert Tuple example / error screenshot here)*

### 🔍 Observation

Attempting to modify a tuple results in a `TypeError` because tuples are immutable.

---

# 💻 Programs Practiced

| Program | Description |
|----------|-------------|
| `01_dunder_variable.py` | Understanding the `__name__` magic variable |
| `02_single_value_container.py` | Reference variables, object creation, and memory behaviour |
| `03_multi_value_container.py` | Multi-value containers, Lists, and Tuples |

---

# 📝 Key Learnings

- Understood the purpose of the `__name__` magic variable.
- Learned how Python programs execute inside a Process.
- Understood the difference between Main Thread and Child Threads.
- Explored Stack and Heap Memory.
- Learned that Python variables are Reference Variables.
- Understood that **Model**, **Container**, and **Object** describe the same concept in different contexts.
- Explored Single Value and Multi Value Containers.
- Compared Lists and Tuples based on mutability.

---

# 📌 Day 2 Summary

Today's session focused on understanding Python's execution model and memory management. We explored how Python programs run inside a process, how tasks are executed using threads, and how memory is divided into Stack and Heap. We also learned how Python variables reference objects stored in memory and studied the concepts of Single Value and Multi Value Containers, along with the behavior of Lists and Tuples.
