# Day 07 Notes
## Recursion, Searching, Sorting and Filtering

---

# Session Objectives

The objective of this session was to:

- Understand the concept of Recursion.
- Visualize how recursive functions execute in memory.
- Learn Stack and Heap memory representation.
- Understand Bubble Sort using VisualGo.
- Study Searching and Filtering techniques.
- Apply Search, Sort, and Filter operations on Flight Data.

---

# 1. Recursion

## Definition

Recursion is a programming technique in which a function calls itself to solve a smaller version of the same problem.

A recursive solution breaks a problem into smaller subproblems until a condition is reached where no further recursive calls are needed.

---

# Components of Recursion

Every recursive function consists of two essential parts:

### 1. Base Condition
The condition that stops the recursive calls.

### 2. Recursive Call
The statement where the function calls itself with a smaller or modified input.

---

# Why Do We Need a Base Condition?

Without a base condition:

- The function keeps calling itself indefinitely.
- New stack frames continue to be created.
- The stack memory eventually becomes full.
- Python raises:

```text
RecursionError: Maximum recursion depth exceeded
```

---

# How Recursion Executes in Memory

Whenever a function is called:

1. A new stack frame is created.
2. Function parameters are stored.
3. Local variables are stored.
4. Execution pauses when another recursive call is made.
5. Control moves to the new function call.

This process continues until the base condition is reached.

After reaching the base condition:

- The most recent function call completes first.
- The stack starts unwinding.
- Results are returned back to previous function calls.

This behavior follows:

## LIFO (Last In First Out)

---

# Stack Memory

The Stack stores:

- Function calls
- Function parameters
- Local variables
- Return addresses
- Execution state of functions

Characteristics:

- Memory is allocated automatically.
- Data is removed automatically when the function finishes.
- Works on the LIFO principle.

---

# Heap Memory

The Heap stores:

- Lists
- Dictionaries
- Sets
- Objects
- Dynamically created data

Characteristics:

- Objects remain in memory until no references exist.
- Multiple variables can refer to the same object.

---

# Memory Representation of Recursion

During recursive execution:

- Multiple stack frames can point to the same object in the heap.
- Only the function parameters and local variables are duplicated.
- The actual data object is not copied unless explicitly created.

This helps reduce memory usage.

---

# Recursive Problems Covered

## 1. get_max()

Purpose:

- Find the maximum element from a collection using recursion.

Concepts Practiced:

- Base condition
- Recursive reduction
- Returning values
- Stack frame creation

---

## 2. product()

Purpose:

- Compute multiplication recursively.

Concepts Practiced:

- Recursive calls
- Return statements
- Problem reduction

---

# Advantages of Recursion

- Produces clean and readable code.
- Suitable for divide-and-conquer problems.
- Useful for tree and graph traversal.
- Helps solve complex problems elegantly.

---

# Disadvantages of Recursion

- Consumes extra stack memory.
- Function calls introduce overhead.
- Can be slower than iterative solutions.
- Incorrect base conditions may cause infinite recursion.

---

# Real-World Applications of Recursion

- File and folder traversal.
- Tree traversal.
- Binary Search.
- Merge Sort.
- Quick Sort.
- Backtracking problems.
- Dynamic Programming.
- Parsing expressions.

---

# Searching

## Definition

Searching is the process of finding a particular element from a collection of data.

The result of searching may be:

- Element found
- Element not found

---

# Linear Search

Linear Search examines each element one by one until the desired element is found.

---

# Characteristics of Linear Search

- Simple to implement.
- Does not require sorted data.
- Suitable for small datasets.
- Sequential in nature.

---

# Time Complexity

### Best Case
O(1)

### Average Case
O(n)

### Worst Case
O(n)

---

# Real-World Use Cases of Linear Search

- Searching contacts in a small phone book.
- Searching a student record.
- Searching products in a small inventory.
- Searching flights by destination.
- Searching by airline name.

---

# Sorting

## Definition

Sorting is the process of arranging data in a specific order.

Common orders:

- Ascending Order
- Descending Order

---

# Why Sorting is Important

Sorting:

- Improves searching efficiency.
- Organizes data.
- Makes analysis easier.
- Improves user experience.

---

# Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

The largest element gradually moves toward the end of the collection after every pass.

---

# Characteristics of Bubble Sort

- Comparison-based algorithm.
- Stable sorting algorithm.
- Easy to understand.
- Inefficient for large datasets.

---

# Time Complexity

### Best Case
O(n)

### Average Case
O(n²)

### Worst Case
O(n²)

---

# Space Complexity

O(1)

---

# Bubble Sort Visualization

Bubble Sort was visualized using:

## VisualGo

VisualGo helped in understanding:

- Comparisons
- Swapping
- Number of passes
- Movement of elements

---

# Filtering

## Definition

Filtering is the process of selecting only those records that satisfy certain conditions.

Filtering does not modify the original data.

Instead, it creates a subset of the data.

---

# Examples of Filtering

- Price less than ₹5000
- Destination equals Delhi
- Non-stop flights only
- Airline equals Indigo

---

# Importance of Filtering

Filtering is widely used in:

- E-commerce websites
- Flight booking systems
- Hotel booking systems
- Banking applications
- Data analytics platforms

---

# Flight Management System Implementation

During the session, Search, Sort, and Filter operations were implemented on flight data.

---

# Search Operations

Examples:

- Search by Flight Number
- Search by Source
- Search by Destination

---

# Sort Operations

Examples:

- Sort by Price
- Sort by Duration
- Sort by Departure Time

---

# Filter Operations

Examples:

- Flights under a certain price
- Flights to a specific destination
- Non-stop flights
- Flights of a particular airline

---

# Learning Outcomes

By the end of this session, we were able to:

✔ Understand recursion and stack frames.

✔ Visualize function execution in memory.

✔ Differentiate between Stack and Heap memory.

✔ Implement recursive solutions.

✔ Understand searching techniques.

✔ Visualize Bubble Sort.

✔ Apply searching, sorting, and filtering on real-world flight data.

✔ Develop problem-solving skills using practical examples.

---

# Key Terms Learned

- Recursion
- Base Condition
- Recursive Call
- Stack Frame
- Stack Memory
- Heap Memory
- Linear Search
- Bubble Sort
- Filtering
- Flight Data Processing
- Search Operation
- Sort Operation
- Filter Operation
