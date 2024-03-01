# Tuple - Collection of items

# List - Collection of items
# mutable -

my_list = [1, 2, 3, 4, 5]
my_list[0] = 21
print(my_list)
print(type(my_list))

# Tuple -
my_tuple = (1, 2, 3, 4, 5)
#my_tuple[0] = 21  # TypeError: 'tuple'
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

new_tup = tuple(my_list)
print(new_tup)