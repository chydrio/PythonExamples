ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

for name, age in ages.items():
  print (name, age)

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

#nested dict
for p_id, p_info in students.items():
    print("\nPerson Name:", p_id)
    for key in p_info:
        print(key + ':', p_info[key])
