#Name classes w/ Pascal WaaaWaaaWaaa
class User:
    #constructor attributes - must include when creating new object. Can provide default value and change when creating.
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user being created...")

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "First Employee")
user_1.followers = 5
#attributes - manually added, better to user constructors
# user_1.id = "001"
# user_1.username = "First_Employee"

print(user_1.username)


user_2 = User("002", "Bob")
# user_2.id = "002"
# user_2.username = "Bob"

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.username)
print(user_2.followers)