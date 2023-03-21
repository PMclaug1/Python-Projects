print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
crossroads = input("You arrive at a cross road. Where do you want to go? Type left or right. ")
if (crossroads.lower() == "right"):
    print("You are eaten by a bear. Game over.")
else:
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim accross. ")

if(lake.lower() == "swim"):
    print("You are swallowed by the Loch Ness monster. Game over.")
else:
    door = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose? ")

if(door.lower() == "yellow"):
    print("You enter a room overflowing with treasure. You have succeeded.")
elif(door.lower() == "blue"):
    print("You step into a cold room and grab a jeweled chalice from a stone altar in the center of the room. You are instantly frozen solid. Game over.")
else:
    print("You step into a room filled with treasure. The stone floor creaks under your feet and you hear a hissing sound. The room ignites with flame and you perish. Game over.")
