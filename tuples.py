empty_tuple = ()
my_tuple = (0, 1, 2, (1, 2, 3), 4, 5, 6)
my_sliced_tuple = my_tuple[0:3]

print(my_tuple)
print(my_tuple[2])
print(my_tuple[3][1])
print(my_sliced_tuple)
print(my_tuple[::2])
print(my_tuple[0:-1])
print(my_tuple[6:3:-1])
