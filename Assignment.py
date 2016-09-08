"""
Elijah Thomas Assignment 1
CP 1404
"""

import math
def main():
    shopping_list_file = open("items.csv", 'r')
    shopping_list = []

    for line in shopping_list_file:
        item, price, priority, status = line.strip().split(',')
        items = [item, float(price), priority, status]
        shopping_list.append(items)
    shopping_list_file.close()
    print("Shopping List 1.0 - by Elijah Thomas")

    menu = "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit"
    menu_input = str(input(menu))
    while menu_input.upper() != "Q":
        if menu_input.upper() == "R":
            print_matching_items(shopping_list, 'r')



        elif menu_input.upper() == "C":
            print_matching_items(shopping_list, 'c')



        elif menu_input.upper() == "A":
            new_item = input("Item name:")
            while new_item.isspace():
                new_item = input("Input can not be blank\nItem name:")
            run = True
            while run == True:
                try:
                    new_item_price = float(input("Price: $"))
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
                    test_priority = new_item_priority/3
                    run = False
                except ValueError:
                    print("Invalid input; enter a valid number")
                except:
                    print("Priority must be 1, 2 or 3")
            while new_item_priority < 1 or new_item_priority > 3:
                new_item_priority = int(input("Priority must be 1, 2 or 3"))
            items = [new_item, new_item_price, new_item_priority, 'r']
            shopping_list.append(items)
            print_matching_items(shopping_list, 'r' or 'c')



        elif menu_input.upper() == "M":
            required_index = print_matching_items(shopping_list, 'r')
            if required_index != False:
                input_valid = False
                while not input_valid:
                    try:
                        item_completed = int(input("Enter the number of an item to mark as completed"))
                        test_item_completed = item_completed * 2
                        input_valid = True
                    except ValueError:
                        print("Invalid input: Enter a number")
                    except:
                       print("Invalid input: Enter a number")
                while item_completed < 0 or item_completed > len(shopping_list):
                    item_completed = int(input("Invalid item number: Enter a number"))
                actual_index = required_index[item_completed]
                shopping_list[actual_index][3] = "c"
                print("{} marked as completed".format(shopping_list[actual_index][0]))



        else:
            print("Invalid menu choice")


        menu_input = str(input(menu))

    shopping_list_file = open('items.csv', 'w')
    for item in shopping_list:
        if item is not shopping_list[-1]:
            shopping_list_file.write("{},{},{},{}\n".format(item[0],item[1], item[2], item[3]))
        else:
            shopping_list_file.write("{},{},{},{}".format(item[0], item[1], item[2], item[3]))
    print("{} items saved to items.csv\nHave a nice day :)".format(len(shopping_list)))
    shopping_list_file.close()

def print_matching_items(list, type):
    """"Takes the shopping list and type of total that needs to be counted as inputs and returns the total (i.e. number of required items, number of completed items or total price)."""
    total = 0
    count = 0
    positions = []
    for item in list:
        if item[3] == type:
            print("{}. {:20}${:6.2f} ({:})".format(count, item[0], item[1], item[2], item[3]))
            count += 1
            total += float(item[1])
            positions.append(list.index(item))
    if type == 'c' and count == 0:
        print("No completed items")
    elif type == 'r' and count == 0:
        print("No required items")
        positions = False
    else:
        print("Total expected price for {} items: ${:.2f}".format(count, total))
    return(positions)

main()
