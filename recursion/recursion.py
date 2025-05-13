data = {
    "name": "Alice",
    "info": {
        "age": 30,
        "contacts": [
            {"type": "email", "value": "alice@example.com"},
            {"type": "phone", "value": "123-456-789"}
        ]
    },
    "projects": [
        {
            "name": "Project A",
            "details": {
                "client": "Company X",
                "contact": {"value": "projectA@example.com"}
            }
        },
        {
            "name": "Project B",
            "details": {
                "client": "Company Y",
                "contact": {"value": "projectB@example.com"}
            }
        }
    ]
}


def find_values_by_key(obj, target_key):
    results = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == target_key:
                results.append(value)  # If the key matches, store the value
            results.extend(find_values_by_key(value, target_key))
    elif isinstance(obj, list):
        for item in obj:
            results.extend(find_values_by_key(item, target_key))

    return results


print(find_values_by_key(data, "value"))

