# Day-09 Notes
# Functions in Class and Circular Doubly Linked List

---

# 1. Functions in Class

Functions defined inside a class are called methods.

Methods operate on the data stored inside the object.

Example purposes of methods:

- Display data
- Modify data
- Delete data
- Return data

---

# 2. Returning Data in Dictionary Format

Objects can return their data as a dictionary.

Benefits:

- Easy to read
- Easy to convert into JSON
- Easy to send through APIs
- Easy to store and manipulate

Example structure:

{
    "title": "Song Name",
    "artist": "Artist Name",
    "duration": "4:30"
}

---

# 3. Song Management System

## Class: Song

Attributes:

- title
- artist
- duration
- next_song
- previous_song

Methods:

- __init__()
- show_song()

---

# 4. Doubly Linked List

Each node contains:

1. Data
2. Next reference
3. Previous reference

Structure:

Previous ← Node → Next

---

# 5. Circular Doubly Linked List (CDLL)

A Circular Doubly Linked List is a doubly linked list where:

- Last node points to first node.
- First node points to last node.

Structure:

Song1 ⇄ Song2 ⇄ Song3    ↓
   
   ↑              
 └─────────────────┘ 
    
---

# Advantages of CDLL

- Traversal in both directions.
- No NULL reference.
- Easy implementation of playlists.
- Efficient insertion and deletion.

---

# 6. Hard-Coded Circular Doubly Linked List

Objects are manually created.

Links are manually established.

Example:

Song1 ⇄ Song2 ⇄ Song3

---

# 7. Dynamic Circular Doubly Linked List

Objects are created during program execution.

Nodes are linked dynamically.

Advantages:

- Flexible
- Scalable
- User-driven

---

# 8. Flight Management System

## Class: Flight

Possible Attributes:

- flight_number
- airline_name
- source
- destination
- departure_time
- arrival_time
- message
- next_flight
- previous_flight
- duration

---

# 9. Operations on Circular Doubly Linked List

## Insertion Operations

### Add at Front
New node becomes the head.

### Add at End
New node becomes the last node.

### Add in Between
Node is inserted between two existing nodes.

---

## Deletion Operations

### Delete from Front
Remove the head node.

### Delete from End
Remove the tail node.

### Delete from Between
Remove a node from the middle.

---

# 10. Applications of Circular Doubly Linked List

- Music Player Playlist
- Browser Navigation
- Image Slideshow
- Flight Navigation System
- Undo and Redo Operations
- Round Robin Scheduling
