patient_name = input("ENTER PSTIENT NAME: ").title()
patient_age = int(input("ENTER PATIENT AGE:"))

i = 1
flag = []
reading = []
c = []

a = int(input(" ENTER NUMBER OF READING: "))

for i in range(a):
    c = int(input(" ENTER READING: "))
    reading.append(c)


def validity(patient_age, patient_heartrate):
    if patient_age > 120 or patient_age < 0:
        flag.append("invalid")

    if patient_heartrate > 180:
        flag.append("warning")


for i in reading:
    validity(patient_age, i)


status = ""

if "invalid" in flag:
    status = "FAIL"
elif "warning" in flag:
    status = "REVIEW"
else:
    status = "PASS"


print(45*"-")
print("CLINICAL DATA RECORD")
print(45*"-")
print("PATIENT NAME:", patient_name)
print("PATIENT AGE :", patient_age)
print("STATUS      :", status)

if "invalid" in flag:
    print("FLAGS       : Invalid input")
else:
    print("FLAGS       : None")

if "warning" in flag:
    print("WARNINGS    : High heart rate detected")
else:
    print("WARNINGS    : None")

print(45*"-")
print("NOTE: THIS RECORD IS FOR DATA ENTRY ONLY")
