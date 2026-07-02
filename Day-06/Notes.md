# Day 06 Notes

# 1. Debugging

Debugging is the process of finding and fixing errors in a program.

### Breakpoint

A breakpoint pauses program execution at a specific line, allowing us to inspect variables and understand program flow.

### Logs

Logs display messages during execution to help track program behavior and identify issues.

---

# 2. Functions

A function is a reusable block of code that performs a specific task.

### Syntax

```python
def function_name():
    statements
```

Example

```python
def greet():
    print("Hello!")

greet()
```

---

# 3. Parameters

Parameters allow values to be passed into a function.

Example

```python
def greet(name):
    print("Hello", name)

greet("Mannat")
```

---

# 4. Default Parameter Values

Default values are used when no argument is provided.

Example

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Mannat")
```

---

# 5. Reference Copy Operation

Python passes object references to functions.

### Single Value Objects (Immutable)

Examples:
- int
- float
- string
- tuple

Modifying them inside a function creates a new object.

---

### Multi Value Objects (Mutable)

Examples:
- list
- dictionary
- set

Changes made inside the function affect the original object.

---

# 6. Memory Representation

Python variables store references to objects in memory.

Understanding memory representation helps explain why immutable objects create new references while mutable objects can be modified directly.

---

# 7. Function Redefinition

A function can be redefined by declaring it again with the same name.

The latest definition replaces the previous one.

Example

```python
def display():
    print("Version 1")

def display():
    print("Version 2")

display()
```

Output

```
Version 2
```

---

# 8. Variable Arguments (*args)

`*args` allows multiple positional arguments.

### Syntax

```python
def add(*args):
    print(args)
```

Example

```python
add(10,20,30)
```

---

# 9. Keyword Arguments (**kwargs)

`**kwargs` allows multiple keyword arguments.

### Syntax

```python
def details(**kwargs):
    print(kwargs)
```

Example

```python
details(name="Mannat", age=20)
```

---

# 10. Deep Copy

Deep copy creates a completely independent copy of an object by creating a new list and copying each element from the original list.

This ensures that changes made to the new list do not affect the original list.

Example

```python
list1 = [10, 20, 30, 40]

list2 = []

for value in list1:
    list2.append(value)

list2.append(50)

print(list1)
print(list2)
```

Output

```
[10, 20, 30, 40]
[10, 20, 30, 40, 50]
```

Here, `list2` is a separate copy of `list1`. Modifying `list2` does not change `list1`.

---

# 11. Return Statement

The `return` statement sends a value back to the caller.

### Syntax

```python
def function():
    return value
```

Example

```python
def square(n):
    return n*n

result = square(5)
print(result)
```

---

# Key Learnings

- Debugging helps identify and fix errors efficiently.
- Functions improve code reusability.
- Parameters make functions flexible.
- Python uses reference copying while passing objects.
- Mutable and immutable objects behave differently.
- `*args` and `**kwargs` allow flexible function arguments.
- Deep copy prevents unintended modifications.
- Return statements enable functions to produce results.
