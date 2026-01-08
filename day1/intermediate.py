a=input("Enter your name: ")
b=int(input("Enter your age: "))
c=input("Enter your city: ")

a=a.title()
c=c.title()
from datetime import datetime
current_year = datetime.now().year
birth_year = current_year - b

print("Hello, my name is " + a + ", I am " + str(b) + "(born in " + str(birth_year) + "), years old and I live in " + c + ".")
if b < 18:
    print("just getting started")
elif 18 <= b < 25:
    print("prime time to shine")
else:
    print("experience meets learning")