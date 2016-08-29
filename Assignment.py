"""
Elijah Thomas Assignment 1
CP 1404
"""
#Ask about try and except and if the input needs to be acquired before the try, only in the try or in the exception as well.
import math
def main():
    shopping_list_file = open("items.csv", 'r')
    shopping_list = []

    number_items = 0
    item_number = 0
    for line in shopping_list_file:
        item, price, priority, status = line.strip().split(',')
        items = [item, float(price), priority, status]
        shopping_list.append(items)
        number_items += 1
        item_number += 1


    print("Shopping List 1.0 - by Elijah Thomas")

    menu = "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit"
    menu_input = str(input(menu))
    while menu_input.upper() != "Q":
        if menu_input.upper() == "R":
            print_matching_items(shopping_list, 'r')
            # for element in shopping_list:
            #     if "r" in element[4]:
            #         print_item(element)
            # print("Total expected price for {} items: ${:.2f}".format(total_calculator(shopping_list, "required"), total_calculator(shopping_list, "price")))

        elif menu_input.upper() == "C":
            for element in shopping_list:
                if "c" in element[4]:
                    print(print_item(shopping_list))
            print("Total expected price for {} items: ${:.2f}".format(total_calculator(shopping_list, "completed"), total_calculator(shopping_list, "price")))

        elif menu_input.upper() == "A":
            new_item = input("Item name:")
            while new_item.isspace():
                new_item = input("Input can not be blank\nItem name:")
            run = True
            while run == True:
                try:
                    new_item_price = int(input("Price: $"))
                    test_value = math.sqrt(new_item_price)
                    run = False
                except ValueError:
                    print("Invalid input; enter a valid number")
                except:
                    print("Invalid input; enter a valid number")
            while new_item_price < 0:
                new_item_price = int(input(("Price must be >= $0\nPrice: $")))

            run = True
            while run == True:
                try:
                    new_item_priority = int(input("Priority:"))
                    while 0 < new_item_priority < 4:
                        new_item_priority = int(input("Priority:"))
                except ValueError:
                    print("Invalid input; enter a valid number")
                except:
                    print("Priority must 1, 2 or 3")
            items = [number_items, new_item, new_item_price, new_item_priority, 'r']
            number_items += 1
            shopping_list.append(items)
            items.clear()
            print("{}, ${:.2f} (priority {}) added to shopping list".format(new_item, new_item_price, new_item_priority))

        elif menu_input.upper() == "M":
            for element in shopping_list:
                print(print_items(shopping_list))
            print("Total expected price for {} items: ${:.2f}".format(number_items, total_calculator(shopping_list, "price")))

            input_valid = False
            while not input_valid:
                try:
                    item_completed = int(input("Enter the number of an item to mark as completed"))
                    item_completed *= 2
                    input_valid = True
                except ValueError:
                    print("Invalid input: Enter a number")
                except:
                   print("Invalid input: Enter a number")
            while shopping_list[0][0] > item_completed > shopping_list[-1][0] or item_completed not in shopping_list[:][0]:
                item_completed = input("Invalid item number")
            shopping_list[item_completed][4] = "c"
            print("{} marked as completed".format(shopping_list[item_completed][1]))

        else:
            print("Invalid menu choice")

        menu = "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit"
        menu_input = str(input(menu))

    for element in shopping_list:
        element.append("\n")
    shopping_list_file.write(shopping_list)
    print("{} items saved to items.csv\nHave a nice day :)".format(len(shopping_list)))

def print_matching_items(list, type):
    """"Takes the shopping list and type of total that needs to be counted as inputs and returns the total (i.e. number of required items, number of completed items or total price)."""
    total = 0
    count = 0
    for item in list:
        if item[3] == type:
            print("{}. {:20}${:6.2f}({:>3})".format(count, item[0], item[1], item[2], item[3]))
            count += 1
            total += float(item[2])
    print("Total expected price for {} items: ${:.2f}".format(count, total))


def print_item(item):
    """returns a formatted version of the shopping list"""
    print("{}. {:20}${:6.2f}({:>3})".format(item[0], item[1], item[2], item[3]))

main()
