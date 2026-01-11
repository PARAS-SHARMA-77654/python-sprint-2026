import json

name = input("ENTER USERNAME:")
balance = int(input("ENTER BALANCE:"))

data = {
    "name": name,
    "balance": balance
}

with open("bank.json", "w") as file:
    json.dump(data, file, indent=4)

print("1-deposit money:")
print("2-withdraw money:")
print("3-exit:")

choice = int(input("enter choice:"))

if choice == 1:
    mon = int(input("enter deposit money:"))
    data["balance"] = data["balance"] + mon

    with open("bank.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Money deposited successfully")

elif choice == 2:
    wi = int(input("enter withdrawal money:"))

    if wi > data["balance"]:
        print("Insufficient balance")
    else:
        data["balance"] = data["balance"] - wi

        with open("bank.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Money withdrawn successfully")

elif choice == 3:
    print("EXIT...........")
    exit()

else:
    print("Invalid choice")
    
    

