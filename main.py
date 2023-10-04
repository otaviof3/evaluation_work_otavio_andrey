# Code made by Otavio and Andrey #
# Import modules #
import stock
import sales
import historic
import menu
# Throughout the program there are multiple error checks, for things like length of dictionary and Try/Except usage, I will not be noting down every one of them, as that would get very repetitive #
def start_variables():
    """ Function that starts the variables of the program """
    product_stock = {}
    changelog = []
    sales_report = {}
    sale_count = 0
    return product_stock,changelog,sales_report,sale_count
def start_program(product_stock,changelog,sales_report,sale_count):
    """ Function that starts the program so that the main only calls functions """
    while True:
        option = menu.market_menu()
        if option == 1:
            product_stock,changelog = stock.add_a_product(product_stock,changelog)
        elif option == 2:
            product_stock,changelog = stock.alter_product_price(product_stock,changelog)
        elif option == 3:
            product_stock,changelog = stock.exclude_a_product(product_stock,changelog)
        elif option == 4:
            historic.view_changelog(changelog)
        elif option == 5:
            product_stock = stock.search_a_product_by_name(product_stock,sales_report)
        elif option == 6:
            product_stock = stock.search_a_category(product_stock)
        elif option == 7:
            stock.view_all_products(product_stock)
        elif option == 8:
            product_stock,sales_report,sale_count = sales.sell_a_product(product_stock,sales_report,sale_count)
        elif option == 9:
            historic.view_sales_report(sales_report)
        else:
            print("Goodbye, have a nice day!")
            break
def main():
    product_stock,changelog,sales_report,sale_count = start_variables()
    start_program(product_stock,changelog,sales_report,sale_count)
main()
