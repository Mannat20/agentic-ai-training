# Day-08 Notes
# Object Oriented Programming (OOP)

---

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that models software using objects.

An object contains:
1. Data (Attributes)
2. Behaviour (Methods)

---

# Two Main Concepts

## 1. Object
An object is anything that exists and has some properties and behaviour.

Examples:
- Bank
- Restaurant
- Student
- Car
- Fan

---

## 2. Class
A class is the blueprint or textual representation of an object.

It defines:
- What data an object will store.
- What operations can be performed on it.

Example:

Bank → Class

HDFC Bank → Object

---

# Principle of OOP

## Step 1
Think of an object.

## Step 2
Draw, represent, or create a textual representation of the object.

## Step 3
Create a real object from that representation.

---

# Real World vs Computer Science World

## Real World

Object:
Anything that exists.

Class:
Architectural drawing or blueprint of an object.

Example:
Building Blueprint → Building.

---

## Computer Science World

Object:
Storage container that holds data.

Class:
Textual representation of how the object will be stored in memory.

---

# Object Storage in Memory

Objects are created inside the Heap Memory.

Variables are created inside the Stack Memory.

The variables in the stack store the address (reference) of objects in the heap.

Example:

bank → 1001
branch → 2001
employees → 3001
employee1 → 4001
employee2 → 5001
employee3 → 6001

---

# Relationship Mapping

## One-to-One (1:1)

One object is associated with only one object.

Example:

Bank → Branch

One bank has one branch.

---

## One-to-Many (1:*)

One object is associated with multiple objects.

Example:

Branch → Employees

One branch can have many employees.

---

# Bank Object Model

## Bank Attributes

- bank_name
- bank_id
- branch

---

## Branch Attributes

- branch_name
- branch_id
- address
- phone
- timings
- employees

---

## Employee Attributes

- employee_id
- name
- designation
- salary
- phone
- email
- address

---

# Memory Representation

Stack:

bank → 1001
branch → 2001
employees → 3001
employee1 → 4001
employee2 → 5001
employee3 → 6001

Heap:

Bank Object
Branch Object
List of Employees
Employee Objects

---

# Mapping Summary

Bank → Branch = One-to-One

Branch → Employees = One-to-Many

---

# Advantages of OOP

- Real-world modelling
- Code reusability
- Easy maintenance
- Better organization
- Scalability
- Modularity
