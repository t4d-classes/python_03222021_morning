

class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0

    def full_name(self):
        return self.first_name + " " + self.last_name


def record_info(self):
    return self.last_name + ", " + self.first_name


person = Person("Bob", "Smith")
person2 = Person("Sally", "Smith")

Person.record_info = record_info

myfn = Person.full_name

print(myfn(person2))

# print(Person)
# print(person)
# print(person.full_name())
# print(person.record_info())

# print(person.first_name)

# print(person.age)

# person.age = 34

# print(person.age)

# del person.first_name

# print(person.first_name)
