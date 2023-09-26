import datetime
# Appends price to the price historic list, is called in the alter price function #
def edit_price_historic(product_stock,name,new_price):
    product_stock[name]["price_historic"].append(new_price)
    return product_stock

# Every edit changelog function appends a message to a list of changes #
# Called when adding a new product #
def edit_changelog_add(name,amount,price,category,changelog):
    changelog.append(f"Product {name} added to stock; amount {amount}; price {price}; category {category}.")
    return changelog

# Called when adding an amount to a product #
def edit_changelog_amount(name,add_amount,product_stock,changelog):
    changelog.append(f"Amount {add_amount} added to product {name}, new total amount {product_stock[name]['amount']}.")
    return changelog

# Called when altering a product's price #
def edit_changelog_alter(name,product_stock,new_price,changelog):
    changelog.append(f"Product {name} price altered from {product_stock[name]['price']} to {new_price}.")
    return changelog

# Called when deleting a product #
def edit_changelog_exclusion(exclusion,changelog):
    changelog.append(f"Product {exclusion} deleted from stock.")
    return changelog

# Shows messages through a for loop #
def view_changelog(changelog):
    for change in changelog:
        print(change)
    enter = input("Press enter to go back to the menu...")

# Used to get sale information in the search a product function #
def filter_sales_report(name,sales_report,product_sales):
    for key, value in sales_report.items():
        if value.get("codename") == name:
            product_sales[key] = value
    return product_sales

# Adds sale information to the sales report #
def edit_sales_report(sales_report,sale_count,name,amount_sold,profit):
    sale_count += 1
    sales_key = str(sale_count) + ". " + name
    sales_report[sales_key] = {
        "amount_sold": amount_sold,
        "profit": profit,
        "sale_time": datetime.datetime.now(),
        "codename": name
    }
    return sales_report,sale_count

# Shows sales information through a for loop #
def view_sales_report(sales_report):
    if len(sales_report) == 0:
        print("No products were sold.")
    else:
        for key in sales_report:
            print("Sale number and product name:",key)
            print("Amount of product that was sold:",sales_report[key]["amount_sold"])
            print("Profit from sale:",sales_report[key]["profit"])
            print("Time of sale:",sales_report[key]["sale_time"])
    enter = input("Press enter to go back to the menu...")