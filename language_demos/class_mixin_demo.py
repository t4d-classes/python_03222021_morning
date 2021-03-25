import json
import yaml

class JsonMixin:

    def to_json(self):
        return json.dumps(self._items)

class YamlMixin:

    def to_yaml(self):
        return yaml.dump(self._items)        

class Parent:

    def __init__(self):
        # single underscore convention means protected
        self._items = []


class Child(Parent, JsonMixin, YamlMixin):

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"List of {len(self._items)} People"

    def append(self, name, age):
        self._items.append({"name": name, "age": age})

    def __add__(self, person):
        self._items.append(person)
        return self

    def __iter__(self):
        return iter(self._items)

    def __next__(self):
        return next(self._items)


child = Child()
child.append("Bob", 34)
child.append("Tim", 23)
child.append("Sally", 21)
child.append("Sri", 67)

print(child.to_json())
print(child.to_yaml())




# child += { "name": "Bob", "age": 34}
# child += { "name": "Sri", "age": 67}

# for person in child:
#     print(person["name"])

# print(child)



