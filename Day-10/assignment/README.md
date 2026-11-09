# Day 10 Assignment - Toll Plaza FastTag Queue

## 🎯 Objective

The objective of this assignment was to model a real-world toll plaza using classes and a circular queue, and to deduct toll tax from a vehicle's FastTag balance.

---

# 📝 Problem Statement

Design a Toll Plaza system in Python.

- A **Vehicle** has a registration number, a type (2W / 4W) and exactly one **FastTag**.
- A **FastTag** has an id, a bank and a balance.
- Vehicles wait in a **Toll Plaza Queue**.
- When a vehicle reaches the booth, the toll is deducted from its FastTag balance.
- If the balance is too low, the toll is not deducted.

---

# 💡 Approach

- `fastTag` and `vehicle` classes are written in `Vehicle_FastTag.py`.
- The `vehicle` class receives a `fastTag` object in its constructor (composition).
- `TollPlazaQueue` in `using_queue.py` stores `front`, `end` and `size`, and links vehicles with `next` and `previous`.
- `tollPlaza.py` creates five vehicles, adds them to the queue, shows the queue and deducts the toll for each one.

---

# 🧠 Concepts Applied

- Classes and Constructors
- Composition (Vehicle has a FastTag)
- Circular Queue
- Referencing Objects using `next` and `previous`
- Conditional Statements
- Importing Classes from Other Files
- `main()` Function

---

# 📂 Logic

```
Create FastTag and Vehicle objects

Add every vehicle to the queue

Show the queue

For each vehicle

    If 4W  -> toll 100 (balance must be > 100)
    Else   -> toll 50  (balance must be > 50)

    If balance is enough

        Deduct toll
        Remove vehicle from the front of the queue

    Else

        Print low balance message

Print the size of the queue
```

---

# 🗂️ Sample Data Used

| Registration No. | Type | FastTag Id | Bank | Balance |
|------------------|------|------------|------|---------|
| PB10AL2937 | 4W | 4019 | SBI | 500 |
| KA12KC1212 | 4W | 7890 | ICICI | 600 |
| HR20AB1122 | 4W | 6609 | ICICI | 50 |
| PB10KC1220 | 4W | 5152 | SBI | 1000 |
| PB10BD3027 | 2W | 2234 | SBI | 20 |

---

# 📷 Output

(Add Toll Plaza Output Screenshot)

---

# 📚 Learning Outcome

Through this assignment, I learned:

- How to connect two classes using composition.
- How a circular queue is built using `next` and `previous` references.
- Splitting a program across multiple files and importing from them.
- Writing business rules (minimum balance) with conditions.

---

# 🚀 Skills Practiced

- Object-Oriented Programming
- Data Structures (Queue)
- Modular Programming
- Problem Solving
- Python Fundamentals

---

# 📌 Conclusion

This assignment applied object-oriented concepts and a circular queue to a practical toll plaza scenario. It showed how real-world entities such as vehicles and FastTags can be represented as objects that work together.
