"""
TASK: Create an Inventory class.

Requirements:
1. Store items in a dictionary (item_name → quantity).
2. Provide a method to add items (with quantity).
3. Provide a method to remove items (only if available).
4. Provide a method to update stock levels.
5. Provide a method to display all inventory items.

Example Usage:
    treasure_store = Inventory()
    favour_store = Inventory()

    treasure_store.add_item("Apples", 50)
    treasure_store.add_item("Bananas", 30)
    treasure_store.remove_item("Apples", 10)
    print(treasure_store.show_inventory())  # {"Apples": 40, "Bananas": 30}

    favour_store.add_item("Milk", 50)
    favour_store.add_item("Garri", 30)
    favour_store.remove_item("Milk", 40)
    print(treasure_store.show_inventory())  # {"Milk": 10, "Garri": 30}
"""


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        """Add a new item or increase its quantity."""
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        """Remove a given quantity of an item (if available)."""
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                print(f"Not enough '{item_name}' in stock to remove {quantity}.")
        else:
            print(f"Item '{item_name}' not found in inventory.")

    def update_stock(self, item_name, new_quantity):
        """Update stock level of an item."""
        if new_quantity < 0:
            print("Quantity cannot be negative.")
            return
        self.items[item_name] = new_quantity

    def show_inventory(self):
        """Return the current inventory as a dictionary."""
        return self.items


# 
treasure_store = Inventory()
favour_store = Inventory()

treasure_store.add_item("Apples", 50)
treasure_store.add_item("Bananas", 30)
treasure_store.remove_item("Apples", 10)
print(treasure_store.show_inventory()) 

favour_store.add_item("Milk", 50)
favour_store.add_item("Garri", 30)
favour_store.remove_item("Milk", 40)
print(favour_store.show_inventory()) 
