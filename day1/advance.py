# CLI-Based Candidate Profile Evaluation System

# -------- INPUT --------
name = input("Enter full name: ")
age_input = input("Enter age: ")
city = input("Enter city: ")
skill = input("Enter primary skill: ")
level = input("Enter skill level (Beginner / Intermediate / Advanced): ")


name=name.title()
city=city.title()

# -------- VALIDATION --------
if name == "":
    print("Error: Name must not be empty.")
    exit()

if not age_input.isdigit():
    print("Error: Age must be a number.")
    exit()

age = int(age_input)

if age < 10 or age > 60:
    print("Error: Age must be between 10 and 60.")
    exit()

if level not in ["Beginner", "Intermediate", "Advanced"]:
    print("Error: Skill level must be Beginner, Intermediate, or Advanced.")
    exit()

# -------- EVALUATION LOGIC --------

# Career Stage
if age < 18:
    career_stage = "Student"
elif age <= 25:
    career_stage = "Early Professional"
else:
    career_stage = "Experienced Professional"

# Readiness Tag & Recommendation
if level == "Beginner":
    readiness = "Foundation Stage"
    recommendation = "Focus on core fundamentals and consistency"
elif level == "Intermediate":
    readiness = "Intern / Junior Ready"
    recommendation = "Start building real-world projects"
else:
    readiness = "Production Ready"
    recommendation = "Contribute to production-grade systems"

# -------- OUTPUT --------
print("\n" + "=" * 45)
print("        CANDIDATE PROFILE CARD")
print("=" * 45)
print(f"Name           : {name.title()}")
print(f"Age            : {age}")
print(f"City           : {city.title()}")
print(f"Primary Skill  : {skill.title()}")
print(f"Skill Level    : {level}")
print("-" * 45)
print(f"Career Stage   : {career_stage}")
print(f"Readiness Tag  : {readiness}")
print(f"Recommendation : {recommendation}")
print("=" * 45)