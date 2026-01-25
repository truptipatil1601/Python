# Initial dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 1. Insert a new key-value pair
my_dict['d'] = 4
print(my_dict)

# 2. Delete a designated key-value pair
del my_dict['b']
print(my_dict)

# 3. Modify the value of a specified key
my_dict['a'] = 10
print(my_dict)

# 4. Verify the existence of a key
print('c' in my_dict)

# 5. Display all keys in the dictionary
print(list(my_dict.keys()))
