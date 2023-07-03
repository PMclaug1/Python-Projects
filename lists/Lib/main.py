numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1

#examples for lists and strings, can be used for other sequences - list, range, string, tuple etc

new_list = [n + 1 for n in numbers]
print(new_list)

name = "Angela"
new_name_list = [letter for letter in name]
print(new_name_list)

double_range = [n * 2 for n in range(1,5)]
print(double_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# square the nubmers list
numbers = [1,1,2,3,5,8,13,21,34,55]

squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

# get even numbers in result
numbers2 = [1,1,2,3,5,8,13,21,34,55]
result = [n for n in numbers2 if n % 2 == 0]
print(result)

# comparing lists is separate files
with open("file1.txt", "r") as file1:
    file1_data = file1.readlines()
with open("file2.txt", "r") as file2:
    file2_data = file2.readlines()

result = [int(n) for n in file1_data if n == n in file2_data]

# Write your code above 👆

print(result)
