name=input("enter your name:")


product_1=input("enter product name:")
price_1=int(input("enter price:"))


product_2=input("enter product name:")
price_2=int(input("enter price:"))



product_3=input("enter product name:")
price_3=int(input("enter price:"))

dict={product_1:price_1,product_2:price_2,product_3:price_3}


sum=price_1+price_2+price_3

if sum>5000 :
    discount=20
elif sum >=2000:
    discount =10
else :
    discount=0






print("-----------------Cart Summary---------------")
print("Username:",name)
print("Product In Cart:")
print(product_1,":",price_1)
print(product_2,":",price_2)
print(product_3,":",price_3)
print("Total Sum:",sum)
print ("Discount:",discount)
print("Final Amount",sum*(100-discount)/100)























