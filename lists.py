empty_list = []
my_list = [0, 1, 2, [1, 2, 3], 4, 5, 6, 7]
my_sliced_list = my_list[0:2]

print(my_list)
print(my_list[2])
print(my_list[3][1])
print(my_sliced_list)
print(my_list[::2])
print(my_list[0:-1])
print(my_list[7:3:-1])

numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
