# Task 1 - Explore the Menu

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

# Step 1 - print menu by category
categories = ["Starters", "Mains", "Desserts"]

for category in categories:
    print("===== " + category + " =====")

    for item_name, details in menu.items():
        if details["category"] == category:
            if details["available"] == True:
                status = "[Available]"
            else:
                status = "[Unavailable]"
            print(item_name, "  Rs.", details["price"], " ", status)

    print("")

# Step 2 - total and available items
total_items = len(menu)
print("Total items on menu :", total_items)

available_count = 0
for item_name, details in menu.items():
    if details["available"] == True:
        available_count = available_count + 1

print("Total available items :", available_count)

# Step 3 - most expensive item
expensive_name  = ""
expensive_price = 0

for item_name, details in menu.items():
    if details["price"] > expensive_price:
        expensive_price = details["price"]
        expensive_name  = item_name

print("Most expensive item :", expensive_name, "- Rs.", expensive_price)

# Step 4 - items under Rs. 150
print("Items under Rs. 150 :")
for item_name, details in menu.items():
    if details["price"] < 150:
        print(item_name, "- Rs.", details["price"])

#----------------------------------------------------------------------------------------------------------

# Task 2 - Cart Operations

cart = []

# Add item logic
def add_item(item_name, quantity):
    if item_name not in menu:
        print(item_name, "does not exist in menu!")
        return
    if menu[item_name]["available"] == False:
        print(item_name, "is not available!")
        return
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = entry["quantity"] + quantity
            print(item_name, "quantity updated in cart!")
            return
    cart.append({
        "item":     item_name,
        "quantity": quantity,
        "price":    menu[item_name]["price"]
    })
    print(item_name, "added to cart!")

# Remove item logic
def remove_item(item_name):
    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            print(item_name, "removed from cart!")
            return
    print(item_name, "is not in cart!")

# Print cart
def print_cart():
    print("Current cart :")
    if len(cart) == 0:
        print("Cart is empty!")
    else:
        for entry in cart:
            print(entry["item"], "x", entry["quantity"], "- Rs.", entry["price"])
    print("")

# Simulate order
add_item("Paneer Tikka", 2)
print_cart()

add_item("Gulab Jamun", 1)
print_cart()

add_item("Paneer Tikka", 1)
print_cart()

add_item("Mystery Burger", 1)
print_cart()

add_item("Chicken Wings", 1)
print_cart()

remove_item("Gulab Jamun")
print_cart()

# Order summary
print("========== Order Summary ==========")
subtotal = 0
for entry in cart:
    item_total = entry["price"] * entry["quantity"]
    subtotal   = subtotal + item_total
    print(entry["item"], "x" + str(entry["quantity"]), "  Rs.", item_total)

gst           = round(subtotal * 0.05, 2)
total_payable = round(subtotal + gst, 2)

print("------------------------------------")
print("Subtotal     : Rs.", subtotal)
print("GST (5%)     : Rs.", gst)
print("Total Payable: Rs.", total_payable)
print("====================================")

#----------------------------------------------------------------------------------------------------------


# Task 3 - Inventory Tracker

import copy

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

# Step 1 - deep copy
inventory_backup = copy.deepcopy(inventory)
print("Backup created!")

# Step 2 - demonstrate deep copy
inventory["Paneer Tikka"]["stock"] = 999
print("Inventory Paneer Tikka stock :", inventory["Paneer Tikka"]["stock"])
print("Backup Paneer Tikka stock    :", inventory_backup["Paneer Tikka"]["stock"])

# restore
inventory["Paneer Tikka"]["stock"] = 10
print("Inventory restored!")
print("")

# Step 3 - deduct cart quantities
for entry in cart:
    item_name     = entry["item"]
    quantity      = entry["quantity"]
    current_stock = inventory[item_name]["stock"]

    if current_stock >= quantity:
        inventory[item_name]["stock"] = current_stock - quantity
        print(item_name, "- deducted", quantity, "units")
    else:
        print("Warning! Not enough stock for", item_name)
        inventory[item_name]["stock"] = 0

print("")

# Step 4 - reorder alerts
print("Reorder Alerts :")
for item_name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print("Reorder Alert:", item_name, "- Only", details["stock"], "unit(s) left (reorder level:", details["reorder_level"], ")")

print("")

# Step 5 - print both to confirm difference
print("Current Inventory :")
for item_name, details in inventory.items():
    print(item_name, "- stock:", details["stock"])

print("")
print("Backup Inventory :")
for item_name, details in inventory_backup.items():
    print(item_name, "- stock:", details["stock"])

#----------------------------------------------------------------------------------------------------------

# Task 4 - Daily Sales Log Analysis

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# then your Task 4 code continues below...
# Step 1 - revenue per day
print("Revenue per day :")
for date, orders in sales_log.items():
    day_total = 0
    for order in orders:
        day_total = day_total + order["total"]
    print(date, "- Rs.", day_total)

print("")

# Step 2 - best selling day
best_day     = ""
best_revenue = 0

for date, orders in sales_log.items():
    day_total = 0
    for order in orders:
        day_total = day_total + order["total"]
    if day_total > best_revenue:
        best_revenue = day_total
        best_day     = date

print("Best selling day :", best_day, "- Rs.", best_revenue)
print("")

# Step 3 - most ordered item
item_count = {}

for date, orders in sales_log.items():
    for order in orders:
        for item in order["items"]:
            if item not in item_count:
                item_count[item] = 0
            item_count[item] = item_count[item] + 1

popular_item  = ""
popular_count = 0

for item, count in item_count.items():
    if count > popular_count:
        popular_count = count
        popular_item  = item

print("Most ordered item :", popular_item, "- ordered", popular_count, "times")
print("")

# Step 4 - add new day and reprint
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print("Updated revenue per day :")
best_day     = ""
best_revenue = 0

for date, orders in sales_log.items():
    day_total = 0
    for order in orders:
        day_total = day_total + order["total"]
    print(date, "- Rs.", day_total)
    if day_total > best_revenue:
        best_revenue = day_total
        best_day     = date

print("Updated best selling day :", best_day, "- Rs.", best_revenue)
print("")

# Step 5 - numbered list of all orders
print("All orders :")
counter = 1

for date, orders in sales_log.items():
    for order in orders:
        items_string = ", ".join(order["items"])
        print(counter, ". [" + date + "] Order #" + str(order["order_id"]) + " - Rs.", order["total"], "- Items:", items_string)
        counter = counter + 1