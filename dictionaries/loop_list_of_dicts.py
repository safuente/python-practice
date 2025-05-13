students = [
    {"name": "Ana", "age": 20, "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "age": 22, "grades": [6.0, 5.5, 7.0]},
    {"name": "Carla", "age": 21, "grades": [9.0, 9.5, 10.0]},
    {"name": "Pablo", "age": 23, "grades": [4.0, 5.0, 6.0]},
]

for student in students:
    grades = student.get('grades')
    name = student.get('name')
    average = sum(grades) / len(grades)
    print(f"{student['name']}: {average:.2f}")
