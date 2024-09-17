my_dict = {'Ivan': 2001, 'Mike': 1996, 'Nastya': 2015}
print('Dict:', my_dict)
print('Existing value:', my_dict['Ivan'])
print('Not existing value:', my_dict.get('Elena', 'Elena is absent in the dictionary'))
my_dict.update({'Lena': 1987, 'Olya': 1955})
Mike_birth = my_dict.pop('Mike')
print('Deleted value:', Mike_birth)
print('Modified dictionary:', my_dict)

my_set = {'ball', True, (25, 4, 9), 'cherry', 'ball', 1}
print('\nSet:', my_set)
my_set.update({100, False})
my_set.discard('ball')
print('Modified set:', my_set)