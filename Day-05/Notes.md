# Day 05 Notes

## 1. Arithmetic Operators

Used for performing mathematical operations.

| Operator | Description | Example |
|----------|-------------|---------|
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| // | Floor Division | a // b |
| % | Modulus | a % b |
| ** | Exponent | a ** b |

---

## 2. Assignment Operators

Assign values to variables.

| Operator | Meaning |
|----------|---------|
| = | Assignment |
| += | Add and Assign |
| -= | Subtract and Assign |
| *= | Multiply and Assign |
| /= | Divide and Assign |
| %= | Modulus and Assign |
| //= | Floor Divide and Assign |
| **= | Power and Assign |

---

## 3. Comparison Operators

Return either True or False.

- ==
- !=
- >
- <
- >=
- <=

---

## 4. Logical Operators

Used to combine conditions.

| Operator | Description |
|----------|-------------|
| and | True if both conditions are True |
| or | True if at least one condition is True |
| not | Reverses the result |

---

## 5. Membership Operators

Check whether an element exists inside a sequence.

- in
- not in

Example

```python
name = "Python"

print("P" in name)
print("Java" not in name)
```

---

## 6. Bitwise Operators

Operate directly on binary values.

| Operator | Meaning |
|----------|---------|
| & | AND |
| \| | OR |
| ^ | XOR |
| ~ | NOT |
| << | Left Shift |
| >> | Right Shift |

Example

```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
```
## Use Cases of Bitwise Operators

Bitwise operators work directly on the binary representation of numbers. They are mainly used in situations where speed and efficient memory usage are important.

### Common Applications

- **Permission Management:** Managing read, write, and execute permissions.
- **Embedded Systems:** Controlling hardware components like LEDs, sensors, and microcontrollers.
- **Networking:** Processing IP addresses, subnet masks, and packet headers.
- **Encryption:** Performing XOR operations for simple encryption and data security.
- **Graphics & Image Processing:** Manipulating pixel values and image masks.
- **Performance Optimization:** Using shift operators (`<<`, `>>`) for fast multiplication and division by powers of 2.

### Key Takeaway

Bitwise operators are preferred when working with binary data, low-level programming, hardware interaction, networking, and performance-critical applications.
---

## 7. Shift Operators

### Left Shift (<<)

Shifts bits to the left.

Formula

```
a << n = a × (2^n)
```

Example

```python
5 << 1 = 10
```

---

### Right Shift (>>)

Shifts bits to the right.

Formula

```
a >> n = a ÷ (2^n)
```

Example

```python
20 >> 2 = 5
```

---

# Conditional Statements

Decision-making constructs in Python.

---

## 1. if Statement

Executes code only when the condition is True.

### Syntax

```python
if condition:
    statement
```

Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

## 2. if-else Statement

Executes one block when the condition is True and another when False.

### Syntax

```python
if condition:
    statement
else:
    statement
```

Example

```python
num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 3. if-elif-else Statement

Used for multiple conditions.

### Syntax

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

Example

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

---

## 4. Nested if

An if statement inside another if statement.

### Syntax

```python
if condition1:
    if condition2:
        statement
    else:
        statement
else:
    statement
```

Example

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible")
    else:
        print("Not a citizen")
else:
    print("Underage")
```

---

# Promo Code Handling Approach

The trainer demonstrated how a real-world e-commerce application validates promo codes.

General approach:

1. Accept user input.
2. Check whether the promo code exists.
3. Validate minimum purchase amount.
4. check discount_upto.
5. Apply discount.
6. Display the final payable amount.

This example demonstrated how nested conditions and logical operators work together in practical applications.

---

# Brick Problem

The assignment focused on solving the Brick Problem using loops and conditional statements.

Concepts used:

- Variables
- Loops
- Conditions
- Logical Thinking
- Problem Decomposition

The primary objective was to develop an algorithm before implementing the code.

---

# Key Learnings

- Operators are the building blocks of expressions.
- Bitwise operators manipulate binary data efficiently.
- Conditional statements control program execution.
- Nested conditions help solve complex real-world scenarios.
- Problem-solving begins with understanding the logic before coding.
