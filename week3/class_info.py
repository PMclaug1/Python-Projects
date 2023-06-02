#Name classes w/ Pascal WaaaWaaaWaaa
class User:
    def __init__(self):
        print("new user being created...")

user_1 = User()
#attributes - manually added, better to user constructors
user_1.id = "001"
user_1.username = "First_Employee"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Bob"