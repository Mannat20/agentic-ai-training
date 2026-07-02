# Day 03 Assignment - Data Modeling using Python Dictionaries

## 🎯 Objective

The objective of this assignment was to observe real-world applications and organize their data using Python dictionaries and nested data structures.

The assignment focused on representing complex UI information in a structured manner without implementing any business logic.

---

# Assignment 1: MakeMyTrip Data Modeling

## 📝 Problem Statement

Analyze the MakeMyTrip flight booking page and organize the displayed information into a well-structured Python dictionary.
![Assignment 1](../images/assignment_1.jpg)

---

## 💡 Approach

The complete flight booking information was represented using **nested dictionaries** to maintain a hierarchical relationship between different sections of the application.

The following components were modeled:

- Flight title
- Coupon offers
- Flight offers (Popular & Cheapest)
- Onward flight details
- Return flight details
- Additional offers and services

---

## 📂 Data Structure Used

```
Dictionary
│
├── title
├── coupon
│   ├── MMTSECUREINT
│   └── ICICIINTEMI
│
├── offer
│   ├── Popular
│   └── Cheapest
│
├── details
│   ├── Onward
│   └── Return
│
└── other_offers
```

---

## 🧠 Key Concepts Applied

- Dictionary
- Nested Dictionary
- Key-Value Mapping
- Hierarchical Data Organization
- Real-world Data Modeling

---

## ❓ Why Dictionary?

A dictionary was selected because it:

- Stores data using meaningful keys.
- Provides fast access to values using keys.
- Represents hierarchical relationships efficiently.
- Is easy to maintain and extend.
- Closely resembles JSON objects used in modern web applications.

---

## 📚 Learning Outcome

Through this assignment, I learned how to:

- Analyze a real-world application interface.
- Break complex UI into logical data components.
- Represent hierarchical information using nested dictionaries.
- Design scalable and readable data models.

---

# Assignment 2: BookMyShow Data Modeling

## 📝 Problem Statement

Study the BookMyShow movie ticket booking interface and organize its seating information using Python data structures.
![Assignment 2](../images/assignment_2.jpg)

---

## 💡 Approach

The theatre seating layout was represented using nested dictionaries.

The data model includes:

- Ticket Categories
- Ticket Price
- Row-wise Seat Arrangement
- Individual Seat Numbers
- Seat Availability Status
- Wheelchair Accessible Seats

---

## 📂 Data Structure Used

```
Dictionary
│
├── CLASSIC
│   ├── price
│   ├── A Row
│   ├── B Row
│   └── C Row
│
└── PRIME
    ├── price
    ├── D Row
    ├── E Row
    └── F Row
```

---

## 🧠 Key Concepts Applied

- Dictionary
- Nested Dictionary
- Hierarchical Data Representation
- Real-world Data Modeling
- Structured Data Organization

---

## ❓ Why Dictionary?

A dictionary was chosen because it:

- Organizes seat categories efficiently.
- Allows quick access to any row or seat.
- Makes updating seat availability simple.
- Provides a scalable structure for larger seating layouts.

---

## 📚 Learning Outcome

This assignment helped me understand how:

- Movie ticket booking systems organize seating information.
- Hierarchical relationships can be represented using nested dictionaries.
- Structured data models simplify data management and future expansion.

---

# 🚀 Overall Concepts Practiced

- Dictionary
- Nested Dictionary
- Key-Value Mapping
- Hierarchical Data Organization
- Real-world Data Modeling
- Structured Programming
- Data Representation

---

# 📁 Files Included

| File | Description |
|------|-------------|
| `makemytrip.py` | Represents the MakeMyTrip flight booking interface using nested dictionaries. |
| `bookmyshow.py` | Represents the BookMyShow theatre seating layout using nested dictionaries. |

---

# 🎯 Skills Gained

- Python Dictionaries
- Nested Dictionaries
- Data Modeling
- Problem Analysis
- Hierarchical Data Representation
- Real-world Application Modeling
- Structured Programming

---

## 📌 Conclusion

This assignment strengthened my understanding of Python dictionaries by applying them to model real-world applications. It demonstrated how hierarchical and structured data can be represented efficiently using nested dictionaries, making the data more organized, scalable, and easier to maintain.
