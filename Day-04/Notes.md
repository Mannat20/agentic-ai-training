# Day 04 Notes

---

# Set in Memory

A Set stores unique and unordered elements.

### Characteristics

- Mutable
- No duplicate values
- Unordered collection
- Implemented using hashing

### Memory Representation

(Add Screenshot)

---

# Dictionary in Memory

Dictionary stores key-value pairs.

### Characteristics

- Mutable
- Keys are unique
- Fast lookup using hashing

### Memory Representation

(Add Screenshot)

---

# Stack Frame

Whenever a function is called,

- A new stack frame is created.
- Local variables are stored inside the frame.
- Frame is destroyed after function execution.

(Add Stack Frame Diagram)

---

# main() Function

Python executes code from top to bottom.

Using

```python
if __name__ == "__main__":
```

ensures that specific code runs only when the file is executed directly.

Benefits

- Better modularity
- Code reusability
- Prevents unintended execution during imports

---

# Number Systems and Memory Address Representation

In Python, every object created in memory has a unique identity, which can be obtained using the built-in `id()` function.

```python
x = 100

print(id(x))
```

**Output (Example)**

```
2398475620880
```

The value returned by `id()` is an integer representing the memory address (or object identity). Since memory addresses are commonly represented in **Hexadecimal**, Python provides functions to convert numbers into different number systems.

---

## Using `hex()` with `id()`

The memory address returned by `id()` can be converted into hexadecimal using the `hex()` function.

```python
x = 100

print(id(x))
print(hex(id(x)))
```

**Output (Example)**

```
2398475620880
0x22e7a67d090
```

Here,

- `id(x)` returns the object's identity.
- `hex(id(x))` converts that identity into hexadecimal format.
- The prefix `0x` indicates a hexadecimal number.

This representation is widely used in debugging, memory visualization, and low-level programming because hexadecimal values are shorter and easier to interpret than large decimal numbers.

---

## Binary Number System (`bin()`)

- Base: **2**
- Digits Used: **0 and 1**

```python
num = 25

print(bin(num))
```

**Output**

```
0b11001
```

The prefix `0b` represents a binary number.

---

## Octal Number System (`oct()`)

- Base: **8**
- Digits Used: **0 to 7**

```python
num = 25

print(oct(num))
```

**Output**

```
0o31
```

The prefix `0o` represents an octal number.

---

## Hexadecimal Number System (`hex()`)

- Base: **16**
- Digits Used: **0–9 and A–F**

```python
num = 255

print(hex(num))
```

**Output**

```
0xff
```

The prefix `0x` represents a hexadecimal number.

---

| Function | Purpose | Example Output |
|----------|---------|----------------|
| `id()` | Returns the unique identity (memory address) of an object | `2398475620880` |
| `hex(id())` | Displays the memory address in hexadecimal format | `0x22e7a67d090` |
| `bin()` | Converts a decimal number to binary | `0b11001` |
| `oct()` | Converts a decimal number to octal | `0o31` |
| `hex()` | Converts a decimal number to hexadecimal | `0xff` |

### Key Takeaway

The `id()` function helps identify the memory location (object identity) of an object. Since memory addresses are conventionally represented in hexadecimal, `hex(id(object))` provides a more readable representation. The `bin()`, `oct()`, and `hex()` functions are useful for converting decimal numbers into different number systems, which are commonly used in computer architecture, debugging, and system-level programming.

---
# Iteration (Loops)

Loops are used to execute a block of code repeatedly. They simplify repetitive tasks and make programs more efficient.

---

# List Iteration

Python provides multiple ways to iterate through a list.

## 1. Index-Based Iteration

This method uses the index position of each element.

### Syntax

```python
for index in range(len(list_name)):
    # Access element using index
```

### Example

```python
fruits = ["Apple", "Mango", "Orange"]

for index in range(len(fruits)):
    print(index, fruits[index])
```

### Advantages

- Access both index and value.
- Useful when updating list elements.

---

## 2. Enhanced For Loop

The enhanced for loop directly accesses each element without using an index.

### Syntax

```python
for element in iterable:
    # Statements
```

### Example

```python
fruits = ["Apple", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)
```

### Advantages

- Simple and readable.
- No need to manage index values.

---

# Dictionary Iteration

Dictionaries can be traversed using keys, values, or key-value pairs.

## Iterating Through Keys

### Syntax

```python
for key in dictionary_name:
    # Statements
```

### Example

```python
student = {
    "name": "Mannat",
    "age": 20
}

for key in student:
    print(key)
```

---

## Iterating Through Values

### Syntax

```python
for value in dictionary_name.values():
    # Statements
```

### Example

```python
for value in student.values():
    print(value)
```

---

## Iterating Through Key-Value Pairs

### Syntax

```python
for key, value in dictionary_name.items():
    # Statements
```

### Example

```python
for key, value in student.items():
    print(key, value)
```

---

# While Loop

A `while` loop executes repeatedly as long as the given condition evaluates to `True`.

### Syntax

```python
while condition:
    # Statements
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Characteristics

- Condition-controlled loop.
- Best suited when the number of iterations is unknown beforehand.
- Ensure the loop condition eventually becomes `False` to avoid an infinite loop.

---

# Nested Loops

Nested loops are loops inside another loop. They are commonly used to process multidimensional data such as matrices, tables, and patterns.

### Syntax

```python
for outer_variable in outer_iterable:
    for inner_variable in inner_iterable:
        # Statements
```

### Example

```python
for row in range(3):
    for column in range(3):
        print("*", end=" ")
    print()
```

### Applications

- Matrix traversal
- Pattern printing
- Chess board representation
- Two-dimensional data processing

---

# Chess Board Pattern

Uses

- Nested loops
- Row index
- Column index

Alternating values create the chess board structure.

(Add Output Screenshot)

---

# Summary

Today's session focused on memory visualization, execution flow, iteration techniques, and nested loop applications.
