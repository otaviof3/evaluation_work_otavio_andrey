""" Module for handling historic for the program's many functions """
import datetime
def edit_price_historic(product_stock,name,new_price):
    """ Appends price to the price historic list, called in the alter price function """
    product_stock[name]["price_historic"].append(new_price)
    return product_stock

def edit_changelog_add(name,amount,price,category,changelog):
    """ Called when adding a new product, appends a message to a list of changes """
    changelog.append(f"Product {name} added to stock; amount {amount}; price {price}; category {category}.")
    return changelog

def edit_changelog_amount(name,add_amount,product_stock,changelog):
    """ Called when adding an amount to a product, appends a message to a list of changes """
    changelog.append(f"Amount {add_amount} added to product {name}, new total amount {product_stock[name]['amount']}.")
    return changelog

def edit_changelog_alter(name,product_stock,new_price,changelog):
    """ Called when altering a product's price, appends a message to a list of changes """
    changelog.append(f"Product {name} price altered from {product_stock[name]['price']} to {new_price}.")
    return changelog

def edit_changelog_exclusion(exclusion,changelog):
    """ Called when deleting a product, appends a message to a list of changes """
    changelog.append(f"Product {exclusion} deleted from stock.")
    return changelog

def view_changelog(changelog):
    """ Shows change messages through a for loop """
    for change in changelog:
        print(change)
    enter = input("Press enter to go back to the menu...")

def edit_sales_report(sales_report,sale_count,name,amount_sold,profit):
    """ Adds sale information to sales report, called in the sales module """
    sale_count += 1
    sales_key = str(sale_count) + ". " + name
    sales_report[sales_key] = {
        "amount_sold": amount_sold,
        "profit": profit,
        "sale_time": datetime.datetime.now(),
        "codename": name
    }
    return sales_report,sale_count

def view_sales_report(sales_report):
    """ Shows sales information through a for loop """
    if len(sales_report) == 0:
        print("No products were sold.")
    else:
        for key in sales_report:
            print("Sale number and product name:",key)
            print("Amount of product that was sold:",sales_report[key]["amount_sold"])
            print("Profit from sale:",sales_report[key]["profit"])
            print("Time of sale:",sales_report[key]["sale_time"])
    enter = input("Press enter to go back to the menu...")
