# Day 12 Notes

---

# User Class

The `user` class represents a person registering in an application.

```python
import hashlib

class user:
    def __init__(self, name=None, phone=None, email=None, password=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
```

- Default values of `None` allow an empty object to be created and filled in later.

## input_details()

```python
def input_details(self):
    self.name = input('Enter Name: ')
    self.phone = input('Enter phone: ')
    self.email = input('Enter email: ')
    self.password = input('Enter password: ')
    self.password = self.encrypt(self.password)
```

- Details are read from the keyboard.
- The password is converted to a hash **before** it is stored in the object.

## show()

Prints the user in one line between two separator lines.

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
name | phone | email | hashed password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

---

# Password Hashing

Passwords should never be saved as plain text. If the data leaks, every password would be visible.

```python
def encrypt(self, data):
    encrypted_data = hashlib.sha256(data.encode()).hexdigest()
    return encrypted_data
```

### Step by step

1. `data.encode()` converts the string into bytes, because the hash function works on bytes.
2. `hashlib.sha256(...)` calculates the SHA-256 hash.
3. `.hexdigest()` returns the hash as a readable hexadecimal string.

### Characteristics of SHA-256

- **One-way**: the original password cannot be recovered from the hash.
- Same input always gives the same output.
- Output is always 64 hexadecimal characters.
- To log in, the entered password is hashed again and compared with the stored hash.

Other algorithms in the same family: SHA-512.

(Add Hash Output Screenshot)

---

# Converting an Object into Other Formats

## to_csv()

```python
def to_csv(self):
    return f'{self.name},{self.phone},{self.email},{self.password}'
```

Used for saving a record as one line in a CSV file.

## to_dictionary()

```python
def to_dictionary(self):
    return vars(self)
```

- `vars(object)` returns all the attributes of an object as a **dictionary**.
- This dictionary can be stored directly in MongoDB as a document.

| Method | Output | Used For |
|--------|--------|----------|
| `to_csv()` | `'john,+91...,john@gmail.com,hash'` | CSV file |
| `to_dictionary()` | `{'name': ..., 'phone': ..., ...}` | MongoDB |

---

# File Helper

A small reusable class that appends records to a file.

```python
class fileHelper:
    def __init__(self, file_name='users.csv'):
        self.file = open(file_name, 'a')

    def write_in_file(self, data):
        self.file.write(f'{data}\n')

    def close_file(self):
        self.file.close()
```

- The file is opened in **append mode** in the constructor, so earlier records stay.
- `write_in_file()` writes one record per line.
- `close_file()` must be called at the end.

Example usage

```python
filehelper1 = fileHelper()
filehelper1.write_in_file(csv_data)
filehelper1.close_file()
```

---

# MongoDB

MongoDB is a **NoSQL document database**. Data is stored as JSON-like documents instead of rows and columns.

| SQL Term | MongoDB Term |
|----------|--------------|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |

A document looks like a Python dictionary.

```
{
  "name": "john",
  "phone": "+91 3422427896",
  "email": "john@gmail.com",
  "password": "<hashed password>"
}
```

## MongoDB Atlas

Atlas is the **cloud-hosted** MongoDB service. A free cluster was created and a database user was added. Atlas provides a **connection URI** of the form:

```
mongodb+srv://<username>:<password>@<cluster-address>/?appName=Cluster0
```

> The password must never be written in code that is pushed to GitHub. Keep it in an environment variable or a separate file that is ignored by Git.

---

# Connecting using PyMongo

```python
from pymongo import MongoClient
from pymongo.server_api import ServerApi
```

- `MongoClient` starts with a capital **M** and **C**, which shows it is a **class**.
- `ServerApi('1')` selects the stable server API version.

## Testing the Connection (mongo.py)

```python
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
```

- `ping` is a lightweight command that checks that the server is reachable.

(Add Connection Success Screenshot)

## Selecting a Database (db.py)

```python
db = client['Agentic_AI']
names = db.list_collection_names()
print(names)
```

- `client['Agentic_AI']` selects the database. MongoDB creates it when data is first stored.
- `list_collection_names()` returns the names of all collections in it. It is a **method**, so it must be called with `()`; without the brackets Python prints the method object instead of the list.

---

# DBHelper Class

Wraps the database code inside a class so the main program stays short.

```python
class DBHelper:
    def __init__(self, db_name='Agentic_AI'):
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client[db_name]
        print('[DBHelper] Connection Created')

    def select_collection(self, collection='users'):
        self.collection = self.db[collection]
        print('[DBHelper] Collection Selected:"', collection)

    def save_document(self, document):
        inserted_id = self.collection.insert_one(document)
        print('[DBHelper] Document Saved. Id is:', inserted_id)
```

| Method | Purpose |
|--------|---------|
| `__init__` | Connects to MongoDB and selects the database |
| `select_collection()` | Chooses the collection (default `users`) |
| `save_document()` | Inserts one document using `insert_one()` |

---

# Putting It Together (implement.py)

```python
user1 = user()
user1.input_details()
user1.show()

csv_data = user1.to_csv()
dict_data = user1.to_dictionary()

dbhelper = DBHelper()
dbhelper.select_collection()
dbhelper.save_document(dict_data)
```

### Flow

```
Keyboard input -> user object -> password hashed
                      |
          +-----------+-----------+
          v                       v
      to_csv()             to_dictionary()
          |                       |
     fileHelper               DBHelper
     (users.csv)            (MongoDB users)
```

In the final version the CSV part is commented out and the data is stored in MongoDB.

(Add MongoDB Atlas Screenshot)

---

# Things to Revisit

- In the `user` constructor, a trailing comma after `self.name = name,` makes the value a **tuple**. This is harmless in the current flow because `input_details()` replaces the value, but the commas should be removed.
- `users.csv` contains sample passwords in plain text. Only hashed passwords should be stored.
- `save_document()` prints the result object; the actual id is available as `inserted_id.inserted_id`.

---

# Summary

Today's session focused on designing a `user` class, hashing passwords, saving data to a file, and storing the same data in a MongoDB Atlas database using a reusable `DBHelper` class.
