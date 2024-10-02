def calculate_structure_sum(data_):
    if isinstance(data_, (list, tuple, set)):
        result = 0
        for k in data_:
            result += calculate_structure_sum(k)
        return result
    elif isinstance(data_, dict):
        return calculate_structure_sum(tuple(data_.items()))
    elif isinstance(data_, (int, float)):
        return data_
    else:
        return len(data_)


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
# Вывод на консоль:99