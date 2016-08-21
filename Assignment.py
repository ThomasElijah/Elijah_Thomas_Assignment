"""
Elijah Thomas Assignment 1
CP 1404
"""
#Figure out items.csv and load items in
def main():
    print("Shopping List 1.0 - by Elijah Thomas")
    menu = "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit"
    menu_input = input(menu)
    menu_input = menu_input.upper
    while menu_input != "Q":
        if menu_input == "R":
            #print required items
            #print total expected price
        elif menu_input == "C":
            #print completed items
            #print total expected price
        elif menu_input == "A":
            new_item = input("Item name: ")
            price = input("Price: $")
            priority = input("Priority: ")
        elif menu_input == "M":
            #print shopping list
            #print total expected price
            #get the number of item to be marked as complete
        else:
            print("Invalid menu choice")
            menu_input = input(menu)
            menu_input = menu_input.upper
    #print number of items added to items.csv
    #print("Have a nice day :)")