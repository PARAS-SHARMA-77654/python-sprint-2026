import json

more = True
while more:
    print("1-view saved credentials:")
    print("2-add new credentials:")
    print("3-update saved credentials:")
    print("4-exit")

    choice = input("enter choice:")

    if choice == "1":
        with open("volt_data.json", "r") as f:
            det = json.load(f)
            print(det)

    elif choice == "2":
        web = input("WEBSITE:")
        user = input("USERNAME:")
        passw = input("PASSWORD:")

        newdata = {
            "website": web,
            "username": user,
            "password": passw
        }

        with open("volt_data.json", "w") as f:
            data = json.load(f)

        data.append(newdata,f)

        

        print("CREDITAL SAVED SUCCESSFULL")

    elif choice == "3":
        with open("volt_data.json", "r") as f:
            data = json.load(f)

        site = input("ENTER WEBSITE TO UPDATE: ")

        for i in data:
            if i["website"] == site:
                i["username"] = input("NEW USERNAME: ")
                i["password"] = input("NEW PASSWORD: ")
                break

        with open("volt_data.json", "w") as f:
            json.dump(data, f)

        print("UPDATED SUCCESSFULLY")

    elif choice == "4":
        print("EXITING...")
        break

    else:
        print("INVALID CHOICE")

#does it work
   
