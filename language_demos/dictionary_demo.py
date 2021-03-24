

# person = dict(first_name="Bob", last_name="Smith")

person = {
    "first_name": "Bob",
    "last_name": "Smith",
    "age": 34,
    "jobs": {
        "programmer": "Sr. Developer",
        "crochet": "Magazine Editor for Crocheting"
    }
}

# person["jobs"]["programmer"]

# person = dict([
#     ("first_name", "Bob"),
#     ("last_name", "Smith"),
# ])

# print(person)

# del person["age"]

# print(person)

# print(person["first_name"])

# person["age"] = 32

# print(person)

for key in person:
    print(key + ": " + str(person[key]))
