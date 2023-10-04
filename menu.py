""" Menu module contains a function for calling the menu """
def market_menu():
    """ The menu, choose an option and it returns the option variable """
    print("    Extra Market ")
    print("--------------------  ")
    print('  Choose an option:     ')
    print('1 - Add a product. ')
    print('2 - Alter product price.')
    print('3 - Exclude a product.')
    print('4 - Changelog.')
    print('5 - Search a product.')
    print('6 - Search a category.')
    print('7 - View all products.')
    print('8 - Sell a product.')
    print('9 - Show sales report.')
    print('-----Type any other number to exit the program-----')
    while True:
        option = input('Type the option you want through the numbers indicated above: ')
        try:
            option = int(option)
        except:
            print("Error! Type a valid option!")
        else:
            break
    return option
