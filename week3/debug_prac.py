def test_funct():
    for i in range(1, 20):
        if i == 20:
            print("You got it.")
test_funct()
# i loops until 19, upper bound is not included in range

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6)
#original above, will get out of bounds error and not include [0] from list
dice_num = randint(0,5)
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth? "))
if year >= 1980 and year < 1994:
    #originally did not have >=, could not evaluate 1980
    print("You are a millenial.")
elif year >= 1994:
    #originally did not have >=, could not evaluate 1994
    print("You are a Gen Z.")

# # Fix the Errors
age = int(input("How old are you?"))
#originally had a 'str' and 'int' error. changed input to INT
if age > 18:
    print(f"You can drive at age {age}.")
    #originally had a block indentation error. was also missing f string

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page = int(input("Number of words per page: "))
#originally had ==, words_per_page would still be 0.
print(word_per_page)
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
#line 48 was not indented. iterated through all of a_list and only appended the last item
  print(b_list)

mutate([1,2,3,5,8,13])