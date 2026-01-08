patient_name=input("ENTER YOUR NAME:")
patient_age=int(input("ENTER YOUR AGE:"))
patient_heartrate=int(input("ENTER YOUR HEARTRATE:"))
patient_sp=int(input("ENTER SYSTOLIC BLOOD PRESSURE:"))
patient_dp=int(input("ENTER DIASTOLIC BLOOD PRESSURE:"))
patient_allergy=input("DO YOU HAVE ANY ALLEGRY(YES/NO):")

flag=[]
Warning=[]

if patient_age<0 or patient_age>120:
    flag.append("invalid age")

if type(patient_heartrate)!=int:
    flag.append("invalid heartrate")

if type(patient_sp)!=int:
    flag.append("invalid systolic BP")

if type(patient_dp)!=int:
    flag.append("invalid diastolic BP")


if patient_dp>patient_sp:
    flag.append("invalid DIASTOLIC >SYSTOLIC")

if patient_allergy!="yes" or patient_allergy!="no":
    flag.append("invalid")

if patient_heartrate>180 or patient_heartrate<40:
    Warning.append("warning")


if patient_dp>130 or patient_dp<40:
     Warning.append("abnormal diastolic BP")



if patient_sp>200 or patient_sp<70:
     Warning.append(" abnormal systolic BP")




status=""
if flag:
    status = "FAIL"
elif   Warning:
    status = "REVIEW"
else:
    status = "PASS"



#copied this audit idea from chatgpt
#copied part start 
import uuid

def generate_audit_number():
    return f"AUD-{uuid.uuid4().hex[:10].upper()}"

ab=generate_audit_number()



from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cd=(timestamp)


#copied part end





print(45*"-")
print(" CLINICAL SYSTEM REPORT")
print(45*"-")

print("AUDIT ID:",ab)
print("TIME STAMP:",cd)
print("NAME:",patient_name)
print("AUDIT STATUS",status)
print("FLAGS:", flag if flag else "None")
print("WARNINGS:", Warning if Warning else "None")   #LOOKED TO DO IT
print("NOTE: This is a non-diagnostic audit report only")
print(45 * "-")



with open("demo.txt", "a") as f:
    f.write("\n" + "-"*50 + "\n")
    f.write(f"Audit ID   : {ab}\n")
    f.write(f"Timestamp  : {cd}\n")
    f.write(f"Name       : {patient_name}\n")
    f.write(f"Status     : {status}\n")
    f.write(f"Flags      : {flag if flag else 'None'}\n")
    f.write(f"Warnings   : {Warning if Warning else 'None'}\n")
    f.write("Disclaimer : Non-diagnostic clinical audit")



    f.close()
