# Self-Assessment Questions
# 1. The most surprising thing about how lists work in Python compared to what I expected is that you can access items from the end of the list without even knowing the list's length if you use negative indices.
# 2. During a business internship, I could use a list to keep track of daily sales easily and it would be simpler to calculate totals and averages without needing to do it all manually in Excel. 

# Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


# Exercise 2
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# Exercise 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are immutable, so coordinates cannot be changed accidentally.")

print(coords)


# Exercise 6
sales = [100, 250, 75, 480, 200]

print("Total:", sum(sales))
print("Count:", len(sales))
print("Average:", sum(sales) / len(sales))
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(prices)
print(discounted)


# Exercise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Average:", sum(high_sales) / len(high_sales))
