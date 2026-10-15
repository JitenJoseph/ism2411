# -- Self-Assessment Questions --
# 1. The first bug I spotted was the missing colon in the second for loop. I found this through the traceback, which showed a syntax error that Python expected a colon. This told me that my current debugging instincts were better at finding syntax errors when Python points them out. However, I also learned that print statements can help find logical errors that don't cause the program to crash and just show errors in calculations (blind errors).
# 2. This function takes the original item price and the customer's membership tier as inputs. Depending on the tier, it applies a different discount, which is 15% for gold, 10% for silver, 5% for bronze, and no discount for any other tier.  Then, it displays the final price after the discount has been added. I think a colleague can use this function without reading its body as long as they knew the tiers and what the function returns.
# 3. AI Disclosure: I used ChatGPT to help explain the SyntaxError and IndexError in Exercise 5, identify the final error in logic, and figure out how to correct them. Overall, I think that AI helped me understand the content better instead of shortcutting it, moreso because I didn't give it my code and solely gave it the error messages to help explain the issues.

# -- Exercise 1 --

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# -- Exercise 2 --

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# -- Exercise 3 --

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold") #used below
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# -- Exercise 4 --

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# -- Exercise 5 --

# broken_sales.py - trace and diagnose before fixing anything.
# I think that the first bug is "total = sale" instead of "total += sale" in the first for loop. The second bug is that the for loop for counting sales is missing a colon at the end of the line. The third bug is that the while loop condition should be "i < len(sales)" instead of "i <= len(sales)" to avoid an IndexError when accessing sales[i] at the last iteration.
# The explanation that ChatGPT gave me was that there is a syntax error because Python expected a colon after "sales", but it was missing, and therefore caused a syntax error. To fix this, I'd add a colon after "sales." For the IndexError, ChatGPT explained that the while loop tried to access an index that wasn't in the sales list. To fix this, I'd change the while loop condition to "i < len(sales)" instead of "i <= len(sales)" so that it doesn't try to access an index that doesn't exist in the list. The final error regards the total, and ChatGPT explained that the total was being set to the current sale instead of adding the current sale to the total. To fix this, I'd change "total = sale" to "total += sale" so that it adds the current sale to the total instead of replacing it.

sales = [120, 80, 250, 175, 90]

total = 0
print("Initial total:", total)

for sale in sales:
    print("Current sale:", sale)
    print("Total before:", total)
    total += sale
    print("Total after:", total)
print(f"Total: ${total}")

count = 0
print("Initial count:", count)

for sale in sales:
    print("Current sale:", sale)
    count += 1
    print("Current count:", count)
print(f"Count: {count}")

i = 0
print("Initial index:", i)
print("Length of sales:", len(sales))

while i < len(sales):
    print("Current index:", i)
    print(sales[i])
    i += 1
    print("Updated index:", i)

# -- Exercise 6 --

x = 100 # apple # Global

def double_it():
    # global x
    x = 999 # local another apple (not the same apple as above)
    return x * 2

print(x)
print(double_it())
print(x)

# The x inside double_it() is local. It doesn't change global x = 100.