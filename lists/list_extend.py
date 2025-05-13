nested_lists = [
    [1, 2, 3],
    [4, 5],
    [6],
    [7, 8, 9, 10]
]

result_lst = []
for nested_list in nested_lists:
    result_lst.extend(nested_list)


print(result_lst)
