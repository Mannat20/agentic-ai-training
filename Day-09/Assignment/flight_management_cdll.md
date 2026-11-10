# Assignment - Flight Management System using Circular Doubly Linked List

## Objective

To implement a Flight Management System using Circular Doubly Linked List and perform insertion and deletion operations.

---

# Class: Flight

## Attributes

- flight_id
- airline_name
- source
- destination
- departure_time
- arrival_time
- fare
- next_flight
- previous_flight

---

# Relationship


Flight1 ⇄ Flight2 ⇄ Flight3 ⇄ Flight4 
                           ↓            
↑└──────────────────────┘

---

# Operations Implemented

## Insertion

### Add Flight at Front

Insert a new flight before the current head.

---

### Add Flight at End

Insert a new flight after the current tail.

---

### Add Flight in Between

Insert a flight between two existing flights.

---

## Deletion

### Delete Flight from Front

Remove the first flight from the list.

---

### Delete Flight from End

Remove the last flight from the list.

---

### Delete Flight from Between

Remove a flight from the middle of the list.

---

# Advantages of Using CDLL in Flight System

- Bidirectional traversal.
- Easy navigation between flights.
- Efficient insertion and deletion.
- Continuous circular navigation.
- Suitable for booking and scheduling systems.

---

# Learning Outcomes

- Understanding of Circular Doubly Linked List.
- Dynamic object creation.
- Node manipulation using references.
- Real-world implementation of linked lists.
- Implementation of insertion and deletion operations.
