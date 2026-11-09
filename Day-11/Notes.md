# Day 11 Notes

---

# File Handling

A file allows a program to store data permanently, even after the program ends.

## Steps to Work with a File

```
Open  ->  Read / Write  ->  Close
```

```python
file = open('file_name', 'mode')
```

## File Modes

| Mode | Meaning | If the file already exists |
|------|---------|----------------------------|
| `'r'` | Read | Reads it (error if missing) |
| `'w'` | Write | **Erases** the old content |
| `'a'` | Append | Keeps old content and adds at the end |

---

# Reading a File

```python
with open('tollPlaza.py') as file:
    lines = file.readlines()
    for line in lines:
        print(line)
```

- `read()` returns the **whole content as one string**.
- `readlines()` returns a **list of lines**.
- Each line already ends with `\n`, and `print()` adds another one, so blank lines appear between lines in the output.

```python
data = file.read()
print(type(data), len(data))       # str

lines = file.readlines()
print(type(lines), len(lines))     # list
```

---

# with Statement

```python
with open('tollPlaza.py') as file:
    ...
```

- The file is **closed automatically** when the block ends.
- Safer than calling `close()` manually, because the file closes even if an error occurs.

---

# Writing a File

```python
file = open('quotes.txt', 'a')     # append mode
quotes = input('enter a quote:')
file.write(f'{quotes} \n')
file.close()
print('Quote added..')
```

- `'a'` is used so earlier quotes are **not erased**.
- Using `'w'` instead would replace the entire file every time the program runs.
- `\n` moves the next quote to a new line.
- `close()` saves and releases the file.

(Add quotes.txt Screenshot)

---

# JSON

**JSON (JavaScript Object Notation)** is a text format used to exchange data between programs. It looks like a Python dictionary but it is actually a **string**.

Python provides the built-in `json` module.

```python
import json

order = {
    'oid': 1,
    'customer': 'John',
    'dishes': 'dal, paneer, roti',
    'amount': 500
}
```

## Dictionary to JSON - `dumps()`

```python
json_order = json.dumps(order)

print(type(json_order))   # <class 'str'>
print(json_order)
```

## JSON to Dictionary - `loads()`

```python
order_dictionary = json.loads(json_order)

print(type(order_dictionary))   # <class 'dict'>
print(order_dictionary)
```

| Function | Direction | Result Type |
|----------|-----------|-------------|
| `json.dumps()` | Dictionary -> JSON | `str` |
| `json.loads()` | JSON -> Dictionary | `dict` |

Easy way to remember: `s` stands for **string**, so `dumps` = dump **to string** and `loads` = load **from string**.

---

# Working with an API

An **API** lets one program request data from another over the internet. Many APIs reply in JSON.

## Flow

```
Python program  --request-->  News API server
Python program  <--JSON-----  News API server
        |
   json.loads()
        |
   Python dictionary  ->  read the fields we need
```

## Code (News Reader)

```python
import requests
import json

newsapi_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
response = requests.get(newsapi_url)

news_json = response.text
news_dictionary = json.loads(news_json)

articles = news_dictionary['articles']
for article in articles:
    print(article['title'])
    print(article['description'])
    print('~' * 30)
```

### Explanation

- `requests.get(url)` sends the request and returns a response.
- `response.text` is the JSON as a **string**.
- `json.loads()` turns the string into a dictionary.
- `news_dictionary['articles']` is a **list of articles**, and each article is a dictionary with keys like `title` and `description`.
- The loop prints a headline and its summary, which is the idea behind news apps like Inshorts.

(Add API Output Screenshot)

### Note on API Keys

An API key identifies and authorizes the user. It should **not be typed directly in the code or pushed to GitHub**. A safer way is to keep it in an environment variable.

```python
import os
api_key = os.getenv('NEWS_API_KEY')
```

---

# Object Analysis Program

A small program that combines **reading** and **writing** files.

## Goal

Find how often each class name is used in `tollPlaza.py` and store the counts in a CSV file.

```python
object = {
    'vehicle': 0,
    'fastTag': 0,
    'TollPlazaQueue': 0
}

file = open('tollPlaza.py', 'r')
lines = file.readlines()
for line in lines:
    for i in object:
        if i in line:
            object[i] += 1

with open('objectanalysis.csv', 'a') as files:
    for i in object:
        data = f'{i},{object[i]}\n'
        files.write(data)
```

### How it works

1. A dictionary stores each name with a counter starting at 0.
2. The source file is read line by line.
3. For every line, each name is checked with `in`, and its counter is increased if it appears.
4. The results are appended to `objectanalysis.csv`, one `name,count` pair per line.

### Output (objectanalysis.csv)

```
vehicle,17
fastTag,11
TollPlazaQueue,2
```

The count is the **number of lines** that mention the name, not the total number of times it appears, because a line is counted once even if the name occurs twice in it.

(Add CSV Screenshot)

---

# Toll Plaza (Continued)

The `TollPlaza` folder (`Vehicle_FastTag.py`, `using_queue.py`, `tollPlaza.py`) is the same application built on Day 10. Here it is used as the **input file** for the object analysis program.

---

# Summary

Today's session focused on reading and writing files, converting data between dictionaries and JSON, fetching live data from an API, and using these together in a small analysis program.
