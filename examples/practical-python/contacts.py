contacts = {
    "number": 3,
    "students": [
        {"name": "Harry Potter", "email": "harry@example.com"},
        {"name": "Ronald Weasley", "email": "ron@example.com"},
        {"name": "Hermione Granger", "email": "hermione@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])