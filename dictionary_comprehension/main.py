import  random
import pandas

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(student_scores)
print(passed_students)

# Get each word from the sentence and how many letters are in it
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {letter:len(letter) for letter in sentence.split()}

print(result)

# convert temps from c to f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:((temp * 9/5) + 32) for (day, temp) in weather_c.items()}

print(weather_f)

#looping through dictionaries
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through data frame - columns less useful than rows
for (key,value) in student_data_frame.items():
    print(value)

#Loop through rows
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

