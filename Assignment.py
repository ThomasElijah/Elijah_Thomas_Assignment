"""
Elijah Thomas Assignment 1
CP 1404
"""
#Figure out items.csv and load items in
def main():
    shopping_list_file = open("items.csv", 'r')
    print("Shopping List 1.0 - by Elijah Thomas")
    menu = "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit"
    menu_input = input(menu)
    menu_input = menu_input.upper
    while menu_input != "Q":
        if menu_input == "R":
            line_num = 0
            for line in shopping_list_file:
                if 'r' in line[-1:-2]:
                    print("{}. {:20}${:6.2f}{}".format(line_num, #item name, item price, item priority
                    line_num += 1
                else:
                    line_num += 1

            #print required items
            #print total expected price

        elif menu_input == "C":
            something
        #print completed items
        #print total expected price

        elif menu_input == "A":
            something
        new_item = input("Item name: ")
        price = input("Price: $")
        priority = input("Priority: ")

        elif menu_input == "M":
            something
        #print shopping list
        #print total expected price
        #get the number of item to be marked as complete

        else:
            print("Invalid menu choice")
            menu_input = input(menu)
            menu_input = menu_input.upper
    #print number of items added to items.csv
    #print("Have a nice day :)")

main()
