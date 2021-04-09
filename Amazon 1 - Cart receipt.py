# Implement a receipt function that takes as an input a cart 
# with items and their corresponding prices, tax and promos and returns the total

def calculate(cart):
    net = 0
    tax = 0
    promo = 0
    total = 0
    for items in cart:
        net += cart[items]["net"]
        tax += cart[items]["tax"]
        promo += cart[items]["promo"]
    total = net + tax - promo
    return total, net, tax, promo

item1 = {"net": 120, "tax": 12, "promo": 2}
item2 = {"net": 110, "tax": 11, "promo": 1}
item3 = {"net": 100, "tax": 10, "promo": 0}

cart = {}

cart[0] = item1
cart[1] = item2
cart[2] = item3

total, net, tax, promo = calculate(cart)

print("\nCart net: ", net)
print("Cart tax: ", tax)
print("Cart promos: ", promo)
print("Cart total: ", total, "\n")
