# Day 11 Assignment - Object Analysis and News Reader

## 🎯 Objective

The objective of this assignment was to practise file handling by analysing a Python source file and saving the result, and to practise JSON and API handling by building a simple news reader.

---

# 📝 Problem Statement

## Part 1 - Object Analysis

Read the `tollPlaza.py` file and find how many lines mention each of these names:

- `vehicle`
- `fastTag`
- `TollPlazaQueue`

Store the result in a CSV file named `objectanalysis.csv`.

## Part 2 - News Reader

Fetch the top headlines from an online news API and print the title and description of every article, similar to the Inshorts app.

---

# 💡 Approach

## Part 1

- Keep the names in a dictionary with a counter for each.
- Read the file with `readlines()` and loop through every line.
- Check each name inside every line using `in`.
- Open `objectanalysis.csv` in append mode and write one `name,count` row per name.

## Part 2

- Send a request using `requests.get()`.
- Convert the response text into a dictionary using `json.loads()`.
- Loop through the `articles` list and print `title` and `description`.

---

# 🧠 Concepts Applied

- File Reading (`open`, `readlines`)
- File Writing and Appending
- `with` Statement
- Dictionaries and Nested Loops
- CSV Format
- JSON (`dumps` and `loads`)
- REST API Request using `requests`

---

# 📂 Logic

```
Create dictionary  {name: 0}

Read tollPlaza.py line by line

    For each name

        If name is in the line

            Increase its counter

Open objectanalysis.csv in append mode

    Write  name,count  for every name
```

---

# 📷 Output

(Add objectanalysis.csv Screenshot)

(Add News Reader Output Screenshot)

---

# 📚 Learning Outcome

Through this assignment, I learned:

- Reading a file and processing its content line by line.
- Producing a simple CSV file using plain file writing.
- Converting an API response into a dictionary and extracting fields.
- Why API keys should be protected.

---

# 🚀 Skills Practiced

- File Handling
- Data Processing
- JSON Handling
- API Integration
- Python Fundamentals

---

# 📌 Conclusion

This assignment showed how Python can analyse its own source files, store results permanently, and fetch live data from the internet. These skills form the base for storing and exchanging data in larger applications.
