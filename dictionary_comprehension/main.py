import  random

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