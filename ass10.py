# Define a list with some elements
my_list = [1, 2, 3, 3, 4, 5]

# Function to convert list to set
def list_to_set(lst):
    return set(lst)

# Function to convert set to list
def set_to_list(st):
    return list(st)

# Perform conversions
converted_set = list_to_set(my_list)
print(converted_set)

converted_list = set_to_list(converted_set)
print(converted_list)
