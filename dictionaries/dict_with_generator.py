def squared_numbers():
    for i in range(10_000_000):
        yield i, i**2


squared_numbers_dict = dict(squared_numbers())
print(squared_numbers_dict)
