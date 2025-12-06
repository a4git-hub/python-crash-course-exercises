import random 

number_list = []

for no in range(1,51):
    random_number = random.randint(1,100)
    number_list.append(random_number)

# Created a sequential list using "list" funciton in single line
# number_list2 = list(range(1,51))
# for val in number_list2:
#     print(val)

# Create a list using list comprehension
# number_list3 = [random.randint(1,100) for val in range(1,51)]
# print(number_list3)

# print(number_list)

# min_number = min(number_list)
# print(min_number)

# max_number = max(number_list)
# print(max_number)

# numbersum = sum(number_list) 
# print(numbersum)

# Printing the list individual items/numbers
# for value in number_list:
#     print(value)


# Print position of the number as well as its respective value in the list
# Position: 1 - Value: 19


# odd_numbers = list(range(1, 21, 2))
# for value in odd_numbers:
#     print(value)

# multiple3 = list(range(3, 31, 3))
# for value in multiple3:
#     print(value)

# cubes = [value**3 for value in range(1,11)]
# print(cubes)

