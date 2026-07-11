# Assignment - Bank Object Mapping

## Objective

To create a Bank Management System using Object-Oriented Programming concepts and understand object relationships and memory representation.

---

# Step 1: Identify Objects

1. Bank
2. Branch
3. Employee

---

# Step 2: Create Classes

## Class: Bank

Attributes:
- bank_name
- bank_id
- branch

---

## Class: Branch

Attributes:
- branch_name
- branch_id
- address
- timings
- phone number
- employees

---

## Class: Employee

Attributes:
- employee_id
- name
- designation
- salary
- phone
- email

---

# Step 3: Relationship Mapping

Bank
│
└── Branch

Branch
│
├── Employee 1
├── Employee 2
├── Employee 3
└── Employee n

---

# Cardinality Mapping

## Bank → Branch

Relationship: One-to-One (1:1)

One Bank has one Branch.

---

## Branch → Employees

Relationship: One-to-Many (1:*)

One Branch has multiple Employees.

---

# Memory Representation

Stack

bank → 1001
branch → 2001
employees → 3001
employee1 → 4001
employee2 → 5001
employee3 → 6001

Heap

1001 → Bank Object
2001 → Branch Object
3001 → Employee List
4001 → Employee Object
5001 → Employee Object
6001 → Employee Object

---

# Object Diagram

Bank
│
└── Branch
      │
      ├── Employee
      ├── Employee
      └── Employee

---

# Conclusion

The Bank System demonstrates:

1. Object creation
2. Class representation
3. One-to-One mapping
4. One-to-Many mapping
5. Object storage in Stack and Heap memory.

This assignment helped in understanding how real-world entities can be converted into software objects using OOP concepts.
