name = input("Enter your full name: ")
roll_number = int(input("Enter roll number: "))
branch = input("Enter branch: ")

subjects = input("Enter your favorite subjects (comma-separated): ").split(",")
subjects = [s.strip() for s in subjects]

marks = {}
for sub in subjects:
    marks[sub] = int(input(f"Enter marks of {sub}: "))

skills = input("Enter technical skills (comma-separated): ").split(",")
skills = {s.strip() for s in skills}

subjects.sort()

total_marks = sum(marks.values())
average_marks = total_marks / len(marks)

highest_subject = max(marks, key=marks.get)

print("Full Name:", name)
print("Roll Number & Branch:", (roll_number, branch))
print("Favorite Subjects (Alphabetical):", subjects)
print("Subject-wise Marks:", marks)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Scoring Subject:", highest_subject)
print("Technical Skills:", skills)


#it works because i pray

