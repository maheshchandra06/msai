# Online Shopping cart

# Step 1: Build the ItemToPurchase class
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.cost()}")

if __name__ == "__main__":

    def purchaseItem(message):
        print(message)
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_price = float(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))
        print()
        return item

    # Step 2: Create two objects of the ItemToPurchase class
    item1 = purchaseItem("Item1")
    item2 = purchaseItem("Item2")

    # Step 3: Add the costs of the two items together and output the total cost
    print("TOTAL COST\n")
    item1.print_item_cost()
    item2.print_item_cost()

    print(f"Total: ${item1.cost() + item2.cost()}")
