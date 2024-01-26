data = {'set': {1, 2, 3}, 'list': [4, 5, 6], 'tuple': (7, 8, 9)}
key_to_remove = 'list'
data[key_to_remove].remove(5)
data['tuple'] += (10,)
data['set'].add(data[key_to_remove][0])
del data[key_to_remove][1]
print(data['tuple'])
print(sorted(data['set']), data[key_to_remove], len(data))