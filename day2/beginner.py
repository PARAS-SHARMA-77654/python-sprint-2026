name =input("enter your name :")
age= int(input("enter your age:"))
subject_1=input("enter favourite subject :")
subject_2=input("enter favourite subject :")
subject_3=input("enter favourite subject :")
roll_no=input("enter roll number :")
branch=input("enter your branch:")
marks_1=int(input("enter your marks in first subject:"))
marks_2=int(input("enter your marks in second subject:"))
marks_3=int(input("enter your marks in third subject:"))

skill_1=input("enter your skill:")
skill_2=input("enter your skill:")
skill_3=input("enter your skill:")

c=[subject_1,subject_2,subject_3]
b={roll_no,branch+"(original)"}
a={subject_1:marks_1,subject_2:marks_2,subject_3:marks_3}
d={skill_1,skill_2,skill_3}

print("----------STUDENT DETAILS------------")
print("NAME:",name)
print("Age :",age)
print("Favorite  Subject :" ,c)
print("Student Info:",b)
print("Marks:",a)
print("Technical skill:",d)