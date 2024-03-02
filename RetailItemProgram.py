import RetailItemClass as re
def main():
    Item1 = re.RetailItem('Jacket', 12, 59.95)
    Item2 = re.RetailItem('Designer Jeans', 40, 34.95)
    Item3 = re.RetailItem('Shirt', 20, 24.95)
    print(f"Item1 details: ")
    print(f"The item description is: {Item1.get_description()}")
    print(f"The items inventory is: {Item1.get_inventory()}")
    print(f"The items cost is: {Item1.get_price()}\n\n")

    print(f"Item2 details: ")
    print(f"The item description is: {Item2.get_description()}")
    print(f"The items inventory is: {Item2.get_inventory()}")
    print(f"The items cost is: {Item2.get_price()}\n\n")

    print(f"Item3 details: ")
    print(f"The item description is: {Item3.get_description()}")
    print(f"The items inventory is: {Item3.get_inventory()}")
    print(f"The items cost is: {Item3.get_price()}\n\n")
main()


