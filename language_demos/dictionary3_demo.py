person = {
    "first_name": "Bob",
    "last_name": "Smith",
    "age": 34,
}

# for key in person:
#     print(person[key])

# for key in person.keys():
#     print(key)

# for val in person.values():
#     print(val)

# for key, val in person.items():
#     print(key, val)

the_keys = person.keys()

print(the_keys)

person["street"] = "123 Oak Lane"

print(the_keys)
