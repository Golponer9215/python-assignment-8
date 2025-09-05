"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""



class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices
        self.cart = {}

    def add_item(self, item, quantity):
        if item in self.prices:
            if item in self.cart:
                self.cart[item] += quantity
            else:
                self.cart[item] = quantity
        else:
            print(f"Item '{item}' not found in price list.")

    def remove_item(self, item, quantity):
        if item in self.cart:
            if self.cart[item] >= quantity:
                self.cart[item] -= quantity
                if self.cart[item] == 0:
                    del self.cart[item]
            else:
                print(f"Not enough quantity of '{item}' to remove.")
        else:
            print(f"Item '{item}' not found in cart.")

    def clear_cart(self):
        self.cart = {}

    def calculate_total(self):
        total = 0
        for item, quantity in self.cart.items():
            total += self.prices[item] * quantity
        return total



prices = {"Shirt": 5000, "Shoes": 12000}
cart = ShoppingCart(prices)

cart.add_item("Shirt", 2)
print(cart.calculate_total())  

cart.remove_item("Shirt", 1)
print(cart.calculate_total())   
