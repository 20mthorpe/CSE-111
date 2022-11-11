student1 = {
    "age": 20,
    "name": "fred",
    "phone_number": "555-5555"
}

student2 = {
    "age": 30,
    "name": "Jenny",
    "phone_number": "777-7777"
}

print("the name of the student is " + student1["name"])

student_list = [student1, student2]

print(student_list)

total_age = 0

for student in student_list:
    total_age += student["age"]
    print(student)

average_age = total_age / len(student_list)

print(average_age)

student_names = ["jed", "jen", "sandy"]

for student_name in student_names:
    print(student_name)

print(student_names[2])

#Go through the loop backwards
i = len(student_names) - 1

while i >= 0:
    print(student_names[i])
    i -= 1

for student_name in reversed(student_names):
    print(student_name)

student_names.append("emily")
student_names.pop(1)
print(student_names)