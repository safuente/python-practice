python_workshop = ["Ana", "Luis", "Marta", "Carlos", "Elena"]
django_workshop = ["Marta", "Elena", "Diego", "Sara", "Luis"]


both_workshop = set(django_workshop).intersection(set(python_workshop))
print(f"Both workshops: {both_workshop}")

one_workshop = set(django_workshop).symmetric_difference(set(python_workshop))
print(f"One workshop: {one_workshop}")

unique_attendees_workshops = set(django_workshop).union(set(python_workshop))
print(f"Unique attendees: {unique_attendees_workshops}")
