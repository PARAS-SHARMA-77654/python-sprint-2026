
user = input("Enter your name: ")
products = {
    1: {"name": "Laptop", "price": 45000, "category": "Electronics"},
    2: {"name": "Mobile", "price": 20000, "category": "Electronics"},
    3: {"name": "Rice", "price": 1200, "category": "Grocery"},
    4: {"name": "Shirt", "price": 1800, "category": "Clothing"}
}


cart_products = []
cart_prices = {}
cart_categories = set()

while True:
    print("Available Products:")
    for key, value in products.items():
        print(key, ".", value["name"], "- ₹", value["price"], "(", value["category"], ")", sep="")


    choice = int(input("Select product number: "))

    product = products[choice]

    cart_products.append(product["name"])
    cart_prices[product["name"]] = product["price"]
    cart_categories.add(product["category"])

    more = input("Do you want to continue shopping? (Y/N): ").upper()
    if more != "Y":
        break


payment = input("\nEnter payment method (UPI/Card/COD): ")


total = sum(cart_prices.values())

# Discount
if total >= 5000:
    discount = 20
elif total >= 2000:
    discount = 10
else:
    discount = 0





status = "Order Successful"

if payment == "COD" and "Electronics" in cart_categories:
    status = "Order Not Allowed (COD + Electronics)"
elif payment == "CARD" and total > 30000:
    discount+=5



final_price = total - total*discount/100

# Summary
print("\n" + "="*35)
print("           PURCHASE SUMMARY")
print("="*35)
print("User       :", user)
print("Products   :", cart_products)
print("Categories :", list(cart_categories))
print("Payment    :", payment)
print("Cart Total :", total)
print("Discount   :", int(discount), "%")
print("Final Price:", final_price)
print("Status     :", status)
print("="*35)