from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    city: str


# Create an instance
p = Person(name="Alice", age=30, city="New York")

# Access fields
print(p.name)   # Alice
print(p.age)    # 30

# Print the object
print(p)        # Person(name='Alice', age=30, city='New York')

# Automatically generates:
# __init__() constructor
# __repr__() string representation
# __eq__() comparison logic

p1 = Person("Alice", 30, "New York")
p2 = Person("Alice", 30, "New York")
p3 = Person("Bob", 25, "London")

print(p1 == p2)  # True (same field values)
print(p1 == p3)  # False (different values)
