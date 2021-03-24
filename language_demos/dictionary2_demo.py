

person = {
    # "first_name": "Bob",
    "last_name": "Smith",
    "age": 34,
}

# print(person["address"])

print(person.get("address"))
print(person.get("first_name"))


if "first_name" not in person:
    person["first_name"] = "Tim"
print(person["first_name"])


print(person.setdefault("first_name", "Tim"))

print(person)

print(person.popitem())

print(person)

print(person.pop("address", "123 Oak Lane"))

print(person)
