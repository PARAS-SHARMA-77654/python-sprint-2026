username=input("ENTER YOUR USERNAME:")
platform=input("ENTER PLATFORM NAME:")
account_type=input("ENTER ACCOUNT TYPE:")


user=[]
user.append(username)

plat_type=(platform,account_type)

user_mapp={}
user_mapp[username]=platform

account_typeset=set()
account_typeset.add(account_type)


#print the output
print("--------------ACCOUNT DATA SUMMARY-----------------")
print("PLATFORM AND TYPE:",plat_type)
print("USER MAPPING:",user_mapp)
print("ACCOUNT TYPES:",account_typeset)