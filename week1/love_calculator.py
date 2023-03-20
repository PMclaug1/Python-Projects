# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

countName1 = 0
countName2 = 0
superName = name1 + name2

for x in superName:
    if x == "T" or x == "t" or x == "R" or x == "r" or x == "U" or x == "u" or x == "E" or x == "e":
        countName1 += 1

for x in superName:
    if x == "L" or x == "l" or x == "O" or x == "o" or x == "V" or x == "v" or x == "E" or x == "e":
        countName2 += 1

display = str(countName1) + str(countName2)
score = int(display)

if score >= 40 and score <= 50:
    print(f"Your score is {display}, you are alright together.")
elif score < 10 or score > 90:
    print (f"Your score is {display}, you go together like coke and mentos.")
else:
    print(f"Your score is {display}.")
    

# can refactor with the below
# count("t") can count occurances in a var
# lower() or upper() for case 