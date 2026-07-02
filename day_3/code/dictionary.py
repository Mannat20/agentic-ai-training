# Dictionary/HashTable
students = {
    101: 'John',
    201: 'Fionna',
    301: 'Jennie',
    401: 'Jim',
    501: 'Jack',
    201: 'Joe',
    601: 'Jennie'
}

# Unique Keys, which can have values in a duplicate manner
print(students, id(students), type(students))

products = {            #Dictionary of dictionaries
    10010123: {
        'name': 'Butter',
        'brand': 'Amul',
        'price': 100
    },
    10010456: {
        'name': 'Whole Wheat Bread',
        'brand': 'Bonn',
        'price': 70
    },
}
chat_messages = [       #list of dictionaries
    {
        'message': 'Hi, How Are You?',
        'from': '9876543210',
        'to': '989898780',
        'at': '26 June, 2026 12:33',
        'status': 'seen'
    }
]
print(chat_messages[0]['message'])