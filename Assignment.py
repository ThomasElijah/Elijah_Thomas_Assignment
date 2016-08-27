"""
Elijah Thomas Assignment 1
CP 1404
"""
#Figure out items.csv and load items in


def main():
    shopping_list_file = open("items.csv", 'r')
    shopping_list = []
    element = []
    number_items = 0
    item_number = 0
    for line in shopping_list_file:
        item, price, priority, status = line.split(',')
        element.append(item_number, item, price, priority, status)
        shopping_list.append(element)
        number_items += 1
        item_number += 1
        element.clear()


    print("Shopping List 1.0 - by Elijah Thomas")
    menu = "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit"
    menu_input = input(menu)
    menu_input = menu_input.upper
    while menu_input != "Q":

        if menu_input == "R":
            for element in shopping_list:
                if "r" in element[4]:
                    print("{}. {:20}${:6.2f}({:>3})".format(element[0], element[1], element[2], element[3]))
            print("Total expected price for {} items: ${:.2f}".format(total_calculator(shopping_list, "required"), total_calculator(shopping_list, "price")))


        elif menu_input == "C":
            for element in shopping_list:
                if "c" in element[4]:
                    print("{}. {:20}${:6.2f}({:>3})".format(element[0], element[1], element[2], element[3]))
            print("Total expected price for {} items: ${:.2f}".format(total_calculator(shopping_list, "completed"), total_calculator(shopping_list, "price")))


        # elif menu_input == "A":
        #     new_item = input("Item name:")
        #
        #
        #         new_item = input("Input can not be blank\nItem name:")
        #     new_item_price = input("Price:")
        #     #use some exceptions
        # new_item = input("Item name: ")
        # price = input("Price: $")
        # priority = input("Priority: ")


        elif menu_input == "M":
            for element in shopping_list:
                print("{}. {:20}${:6.2f}({:>3})".format(element[0], element[1], element[2], element[3]))
            print("Total expected price for {} items: ${:.2f}".format(number_items, total_calculator(shopping_list, "price")))
            item_completed = input(print("Enter the number of an item to mark as completed"))
            input_valid = False
            while not input_valid:
                try:
                    item_completed *= 2
                    input_valid = True
                except ValueError:
                    item_completed = input("Invalid input: Enter a number")
                except:
                    item_completed = input("Invalid input: Enter a number")
            while shopping_list[0[0]] > item_completed > shopping_list[-1[0]] or item_completed not in shopping_list[[0]]:
                item_completed = input(print("Invalid item number")
        #print shopping list
        #print total expected price
        #get the number of item to be marked as complete


        else:
            print("Invalid menu choice")
            menu_input = input(menu)
            menu_input = menu_input.upper

    print("{} items saved to items.csv\nHave a nice day :)".format(len(shopping_list)))


    def total_calculator(list, type):
        """"Takes the shopping list and type of total that needs to be counted as inputs and returns the total (i.e. number of required items, number of completed items or total price)."""
        total = 0
        if type == "required":
            for i in list:
                if i[4] == "r":
                    total += 1
        elif type == "completed":
            for i in list:
                if i[4] == "c"
                    total += 1
        elif type == "price":
            for i in list:
                total += int(i[2])
        return(total)





main()
