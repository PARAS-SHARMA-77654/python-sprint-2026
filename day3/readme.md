🛒 Smart CLI Shopping System (Python Mini Project)

A menu-driven, command-line shopping system built using Python.
This project simulates a real-world shopping and checkout flow with products, cart management, discounts, payment rules, and business restrictions.
📌 Project Objective

To build a CLI-based shopping system that demonstrates:

    Use of Python core concepts
    Real-life business logic
    Clean input/output handling
    Conditional decision-making

This project is designed as an intermediate-level Python mini project.
🧠 Concepts Used

    Variables & Data Types
    if / elif / else conditional statements
    Dictionaries, Lists, Sets
    Loops
    User input & validation
    Basic business rule implementation

⚙️ Features
✅ Product Management

    Predefined product catalog
    Each product has:
        Product ID
        Name
        Price
        Category (Electronics / Grocery / Clothing)

✅ Shopping Cart

    User selects products using Product IDs
    Quantity selection
    Automatic cart total calculation
    Category tracking

✅ Discount Rules
Cart Total 	Discount
≥ ₹5000 	20%
≥ ₹2000 	10%
< ₹2000 	0%

Bonus Discount

    Card payment + total > ₹30,000 → extra 5% discount

✅ Payment Rules

    Allowed methods: UPI / Card / COD
    COD is NOT allowed for Electronics

✅ Final Purchase Summary

Displays:

    Customer name
    Itemized cart
    Categories purchased
    Payment method
    Total amount
    Discount applied
    Final payable amount
    Order status

🚫 Business Restrictions

    Duplicate product IDs are not allowed
    Invalid inputs are handled gracefully
    Empty cart checkout is prevented
    COD + Electronics → Order Not Allowed
