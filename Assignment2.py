print("================================")
print(" E-COMMERCE SYSTEM ")
print("================================")

# Login Section

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    role = "Admin"

elif username == "customer" and password == "cust123":
    role = "Customer"

elif username == "cashier" and password == "cash123":
    role = "Cashier"

else:
    print("Invalid username or password")
    exit()

print("\nLogin Successful")
print("Role:", role)

# Access Levels

if role == "Admin":
    print("Access Level: Full Access")

elif role == "Customer":
    print("Access Level: Purchase Products")

else:
    print("Access Level: Process Sales")

print("\n===== PRODUCT PURCHASE =====")

subtotal = float(input("Enter product subtotal: "))

# Coupon Code Section

coupon = input("Enter coupon code: ")

discount = 0

if coupon == "SAVE10":
    discount = subtotal * 0.10
    print("10% discount applied")

elif coupon == "SAVE20":
    discount = subtotal * 0.20
    print("20% discount applied")

elif coupon == "SAVE30":
    discount = subtotal * 0.30
    print("30% discount applied")

else:
    print("Invalid coupon code")
    discount = 0

# Extra Discount Based On Subtotal

if subtotal >= 500000:
    extra_discount = subtotal * 0.05
    print("Extra 5% discount awarded")

else:
    extra_discount = 0

total_discount = discount + extra_discount

amount_after_discount = subtotal - total_discount

# Tax Based On Location

print("\nLocations")
print("1. Uganda")
print("2. Kenya")
print("3. Tanzania")

location = input("Choose location: ")

if location == "1":
    tax_rate = 0.18
    country = "Uganda"

elif location == "2":
    tax_rate = 0.16
    country = "Kenya"

elif location == "3":
    tax_rate = 0.18
    country = "Tanzania"

else:
    tax_rate = 0
    country = "Unknown"

tax = amount_after_discount * tax_rate

final_price = amount_after_discount + tax

# Receipt

print("\n==============================")
print(" E-COMMERCE RECEIPT")
print("==============================")

print(f"User Role: {role}")
print(f"Country: {country}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {total_discount:.2f}")
print(f"Amount After Discount: {amount_after_discount:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Final Price: {final_price:.2f}")

print("==============================")
print("Thank You For Shopping")
print("==============================")