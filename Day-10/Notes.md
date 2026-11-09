# Day 10 Notes

---

# Strings

A string is a sequence of characters used to store text.

## Creating Strings

```python
cafe_name = 'Johns Cafe'          # single quotes
cafe_name = "John's Cafe"         # double quotes (allows an apostrophe)
cafe_name = 'John\'s Cafe'        # escape character \
```

Triple quotes are used for **multi-line** strings.

```python
cafe_name = """Johns Cafe
Redwood Shores
+91 98765 12345
"""
```

| Quote Style | Use |
|-------------|-----|
| `'...'` | Normal text |
| `"..."` | Text that contains a single quote |
| `"""..."""` | Multi-line text |
| `\'` | Escape a quote inside the same quote type |

---

# Strings are Immutable

- A string **cannot be changed** after it is created.
- Every manipulation creates a **new string in memory**.

```python
names = 'john, jennie, jim, jack, joe'
upper_case_names = names.upper()

print(id(names))
print(id(upper_case_names))
```

The two `id()` values are different, which proves that `upper()` returned a new object instead of modifying `names`.

(Add Screenshot)

Other methods of the same kind: `lower()`, `capitalize()`.

---

# split()

`split()` breaks a string into a **list** using a separator.

```python
names = 'john, jennie, jim, jack, joe'
print(names.split(', '))
```

**Output**

```
['john', 'jennie', 'jim', 'jack', 'joe']
```

### Use Case - Finding Keywords in an Order

```python
order = 'i want to order chai samosa with pakora'
keywords = order.split(' ')

if 'chai' in keywords:
    print('What kind of Tea you want ?')
```

- The sentence is split into words.
- The `in` operator checks whether a keyword is present in the list.

---

# Indexing

Every character in a string has an index starting from **0**.

```python
vehicle_reg_number = 'PB10AL2937'
```

| P | B | 1 | 0 | A | L | 2 | 9 | 3 | 7 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

```python
print(vehicle_reg_number[0])                          # P
print(vehicle_reg_number[len(vehicle_reg_number)-1])  # 7
print(vehicle_reg_number[-1])                         # 7
print(vehicle_reg_number[-2])                         # 3
```

- **Positive indexing** counts from the start.
- **Negative indexing** counts from the end, so `-1` is always the last character.

---

# Slicing

Syntax

```python
string[start:stop:step]
```

- `start` is included.
- `stop` is **excluded**.

```python
print(vehicle_reg_number[0:2])   # PB       -> state code
print(vehicle_reg_number[2:4])   # 10       -> district code
print(vehicle_reg_number[4:])    # AL2937   -> from index 4 to the end
print(vehicle_reg_number[:5])    # PB10A    -> from the start to index 4
```

### Reversing a String

```python
print(vehicle_reg_number[::-1])  # 7392LA01BP
```

A step of `-1` walks through the string backwards. This is the **Pythonic** way to reverse a string.

---

# Concatenation and Repetition

```python
full_name = 'John' + ' ' + 'Watson'
print(f'Full Name is: {full_name}')

line = '=' * 60
print(line)
```

- `+` joins strings.
- `*` repeats a string and is handy for drawing separator lines.

---

# strip(), lstrip() and rstrip()

| Method | Removes |
|--------|---------|
| `strip()` | Characters from both ends |
| `lstrip()` | Characters from the left end |
| `rstrip()` | Characters from the right end |

By default whitespace is removed, but a specific character can also be given.

```python
bill_amount = '23.45000'.rstrip('0')
print(bill_amount)
```

**Output**

```
23.45
```

---

# Simple Validation Idea

A basic check on an email and password can be written with string operations.

```python
if '@' in email and '.' in email and len(password) > 8:
    print('Valid email and Valid Password')
else:
    print('InValid email or Password')
```

For real validation, **regular expressions (regex)** are used, for example to validate a vehicle registration number.

---

# String Formatting

Three ways to put values into a string.

```python
customer_name = 'John'
customer_phone = '+91 98765 12345'

customer = {
    'customer_name': 'John',
    'customer_phone': '+91 98765 12345'
}
```

### 1. f-string

```python
print(f'Customer Details: {customer_name} | {customer_phone}')
```

### 2. format() with positions

```python
print('Customer Details: {1} | {0}'.format(customer_name, customer_phone))
```

- `{0}` is the first argument and `{1}` is the second.
- Changing the numbers changes the order, so this prints the phone number first.

### 3. format_map() with a dictionary

```python
print('Customer Details: {customer_name} | {customer_phone}'.format_map(customer))
```

- Placeholders use the **dictionary keys**.
- Very useful when the data already comes as a dictionary (for example from a database).

| Method | Best For |
|--------|----------|
| f-string | Simple, readable formatting |
| `format()` | Reordering values by position |
| `format_map()` | Filling a template from a dictionary |

---

# Toll Plaza Application

Scenario: vehicles with a FastTag arrive at a toll plaza and wait in a queue. Toll is deducted from the FastTag balance.

## Classes

```
FastTag                 Vehicle
-------                 -------
fastTag_id              registration_number
Bank                    type  (2W / 4W)
Balance                 fastTag  ---> 1 FastTag
show()                  show()
```

**1 Vehicle has 1 FastTag.** This is called **composition**, because the `Vehicle` object stores a `FastTag` object inside it.

```python
vehicle1 = vehicle(
    registration_number='PB10AL2937',
    type='4W',
    fastTag=fastTag(fastTag_id=4019, Bank='SBI', Balance=500)
)
```

---

## TollPlazaQueue (Circular Queue)

The queue keeps references to the `front` and the `end` vehicle, and every vehicle points to the `next` and `previous` vehicle.

```
   +-------------------------------------------+
   v                                           |
[ v1 ] <-> [ v2 ] <-> [ v3 ] <-> [ v4 ] <-> [ v5 ]
 front                                       end
   |                                           ^
   +-------------------------------------------+
```

- `end.next` points back to `front`.
- `front.previous` points to `end`.

(Add Queue Diagram)

### Methods

| Method | Purpose |
|--------|---------|
| `add(vehicle)` | Adds a vehicle at the end and links it to the front |
| `deduct_toll_tax(vehicle)` | Deducts toll if the balance is enough |
| `delete()` | Removes the front vehicle from the queue |
| `show(traverse=True)` | Prints all vehicles, forward or backward |

### Toll Rules in the Code

| Vehicle Type | Toll | Condition |
|--------------|------|-----------|
| 4W | ₹100 | Balance must be more than 100 |
| Others (2W) | ₹50 | Balance must be more than 50 |

If the balance is not enough, a **low balance** message is printed and the vehicle stays in the queue.

### Traversal

```python
vehicle = self.front
while True:
    vehicle.show()
    vehicle = vehicle.next
    if vehicle == self.front:
        break
```

Because the queue is circular, the loop stops when it reaches the `front` again.

---

# Things to Revisit

- In `deduct_toll_tax()` the check is `vehicle.type == '4w'` (small w), but the data uses `'4W'` (capital W). The condition is never true, so every vehicle currently goes through the second branch and pays ₹50.
- `delete()` always removes the **front** vehicle, even if a different vehicle was the one charged.
- `next` and `previous` are added to the vehicle object only when it joins the queue; they are not declared in the `vehicle` class.

(Add Output Screenshot)

---

# Summary

Today's session focused on string handling (creation, immutability, indexing, slicing, formatting) and on applying classes, composition and a circular queue to build the Toll Plaza application.
