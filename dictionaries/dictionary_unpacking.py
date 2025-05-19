dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
new_dict = {**dict1, **dict2}
print(new_dict)  # {'a': 1, 'b': 3, 'c': 4}
