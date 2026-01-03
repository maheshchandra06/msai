# Online Shopping cart

import os
import builtins
from typing import List

def print_centered(text):
    width = 0
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80
    print(text.center(width))

# Step 1: Build the ItemToPurchase class
class ItemToPurchase:
    # def __init__(self):
    #     self.item_name = "none"
    #     self.item_price = 0
    #     self.item_quantity = 0
    #     self.item_description=""

    def __init__(self,item_name="none",item_price=0,item_quantity=0,item_description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description=item_description


    def cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        print_centered(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.cost()}")

# Step 4: Build the Shopping cart
class ShoppingCart:
    def __init__(self, customer_name="none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items: List[ItemToPurchase] = []

    def add_item(self, item_to_purchase: ItemToPurchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        try:
            for item in self.cart_items:
                if item.item_name == item_name:
                    self.cart_items.remove(item)
                    break
        except ValueError:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self,item:ItemToPurchase):
        item_found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                item_found = True
                if item != ItemToPurchase():
                    cart_item.item_name = item.item_name
                    cart_item.item_quantity = item.item_quantity
                    cart_item.item_price = item.item_quantity
                print("Modified Item: ",cart_item)
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.cost()
        return total_cost

    def print_total(self):
        if len(self.cart_items) < 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print_centered(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print_centered(f"Number of Items: {self.get_num_items_in_cart()}")

            for item in self.cart_items:
                item.print_item_cost()
            print_centered(f"Total: {self.get_cost_of_cart()}")
            print()

    def print_descriptions(self):
        print_centered(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print_centered("Item Descriptions")
        for item in self.cart_items:
            print_centered(f"{item.item_name}: {item.item_description}")
        print()

if __name__ == "__main__":

    def purchaseItem(message=""):
        print(message)
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_price = float(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))
        print()
        return item


    # step 6: Implement cart menu
    def print_menu(cart: ShoppingCart):
        menu_action = ""
        #Step 5: build menu for shopping cart
        while menu_action not in ['a', 'r', 'c', 'i', 'o', 'q']:
            print_centered("MENU")
            print_centered("a - Add item to cart")
            print_centered("r - Remove item from cart")
            print_centered("c - Change item quantity")
            print_centered("i - Output items' descriptions")
            print_centered("o - Output shopping cart")
            print_centered("q - Quit")
            menu_action = input("Choose an option: ")
            if menu_action == 'q':
                break

        if menu_action == 'o':
            print_centered("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        else:
            print("To be Added!")


    # Step 2: Create two objects of the ItemToPurchase class
    # item1 = purchaseItem("Item1")
    # item2 = purchaseItem("Item2")

    # Step 3: Add the costs of the two items together and output the total cost
    # print("TOTAL COST\n")
    # item1.print_item_cost()
    # item2.print_item_cost()

    # print(f"Total: ${item1.cost() + item2.cost()}")

    cart = ShoppingCart("John Doe", "February 1, 2020")
    item1 = ItemToPurchase("Nike Romaleos", 189, 2, "Volt color, Weightlifting shoes")
    item2 = ItemToPurchase("Chocolate Chips", 3, 5, "Semi-sweet")
    item3 = ItemToPurchase("Powerbeats 2 Headphones", 128, 1, "Bluetooth headphones")

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    print()
    cart.print_total()
    cart.print_descriptions()

    print_menu(cart)
