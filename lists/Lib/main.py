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


