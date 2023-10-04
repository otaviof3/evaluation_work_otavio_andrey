""" Module for handling the many interactions you can have with the market stock """
import historic
def add_a_product(product_stock,changelog):
    """ Checks if the product informed is already in stock or not, if it isn't, adds it and it's amount, price and category through the structure requested, if it is, add informed amount to product stock """
    name = input("Name of the product you want to be added: ").capitalize()
    if name in product_stock:
        while True:
            add_amount = input("Amount to be added to product stock: ")
            try:
                add_amount = int(add_amount)
                if add_amount < 0:
                    print("Error! Type a value of 0 or higher.")
                else:
                    break
            except:
                print("Error! Type a valid amount!")
        product_stock[name]["amount"] += add_amount
        if add_amount != 0:
            changelog = historic.edit_changelog_amount(name,add_amount,product_stock,changelog)
        enter = input("Press enter to go back to the menu...")
        return product_stock,changelog
    else:
        while True:
            amount = input('Amount of product in stock: ')
            try:
                amount = int(amount)
                if amount < 0:
                    print("Error! Type a value of 0 or higher.")
                else:
                    break
            except:
                print("Error! Type a valid amount!")
        while True:
            price = input('Price of product: ')
            try:
                price = float(price)
                if price <= 0:
                    print("Error! Type a value higher than 0.")
                else:
                    break
            except:
                print("Error! Type a valid price!")
        price_historic = [price]
        category = input("Product category: ").capitalize()
        changelog = historic.edit_changelog_add(name,amount,price,category,changelog)
        product_stock[name]= {
            "amount": amount,
            "price": price,
            "price_historic": price_historic,
            "category": category
            }
        enter = input("Press enter to go back to the menu...")
        return product_stock,changelog

def alter_product_price(product_stock,changelog):
    """ Functions that changes the price of the product """
    if len(product_stock) == 0:
        print("No product found in stock.")
    else:
        while True:
            name = input("Name of the product you want to change the price of: ").capitalize()
            if name not in product_stock:
                print("Error! Product not found.")
            else:
                break
        while True:
            new_price = input("Type new price: ")
            try:
                new_price = float(new_price)
                if new_price <= 0:
                    print("Error! Type a value higher than 0.")
                elif new_price == product_stock[name]["price"]:
                    print("Error! Informed price is the same as current price.")
                else:
                    break
            except:
                print("Error! Type a valid price!")
        product_stock = historic.edit_price_historic(product_stock,name,new_price)
        changelog = historic.edit_changelog_alter(name,product_stock,new_price,changelog)
        product_stock[name]["price"] = new_price
    enter = input("Press enter to go back to the menu...")
    return product_stock,changelog

def exclude_a_product(product_stock,changelog):
    """ Deletes a product through the use of the pop function """
    if len(product_stock) == 0:
        print("No products found in stock.")
    else:
        while True:
            exclusion = input("Name the product you want to exclude: ").capitalize()
            if exclusion not in product_stock:
                print("Error! Product not found.")
            else:
                break
        changelog = historic.edit_changelog_exclusion(exclusion,changelog)
        product_stock.pop(exclusion)
    enter = input("Press enter to go back to the menu...")
    return product_stock,changelog

def search_a_product_by_name(product_stock,sales_report):
    """ Searches the product and displays a multitude of informations from it """
    if len(product_stock) == 0:
        print("No products found in stock.")
    else:
        while True:
            name = input("Name of the product to search: ").capitalize()
            if name not in product_stock:
                print("Error! Product not found.")
            else: 
                break
        print("Product name:",name)
        if product_stock[name]["amount"] == 0:
            print("Product out of stock.")
        else:
            print("Product amount in stock:",product_stock[name]["amount"])
        print("Product price:",product_stock[name]["price"])
        if len(product_stock[name]["price_historic"]) > 1:
            print("All prices product has had:")
            for value in product_stock[name]["price_historic"]:
                print(value)
        print("Product category:",product_stock[name]["category"])
        product_sales = filter(lambda item: item[1]["codename"] == name, sales_report.items())
        product_sales = dict(product_sales)
        if len(product_sales) != 0:
            for key in product_sales:
                print("Sale number and product name:",key)
                print("Amount of product that was sold:",product_sales[key]["amount_sold"])
                print("Profit from sale:",product_sales[key]["profit"])
                print("Time of sale:",product_sales[key]["sale_time"])
    enter = input("Press enter to go back to the menu...")
    return product_stock

def search_a_category(product_stock):
    """ Displays every product from a category """
    function_specific_count = 0
    if len(product_stock) == 0:
        print("No products found in stock.")
    else:
        while True:
            category = input(("Category to search: ")).capitalize()
            for key in product_stock:
                if product_stock[key]["category"] == category:
                    function_specific_count += 1
                    print("Product name:",key)
                    if product_stock[key]["amount"] == 0:
                        print("Product out of stock.")
                    else:
                        print("Product amount in stock:",product_stock[key]["amount"])
                    print("Product price:",product_stock[key]["price"])
                    if len(product_stock[key]["price_historic"]) > 1:
                        print("All prices product has had:")
                        for value in product_stock[key]["price_historic"]:
                            print(value)
            if function_specific_count == 0:
                print("No product with matching category found.")
            else:
                break
    enter = input("Press enter to go back to the menu...")
    return product_stock

def view_all_products(product_stock):
    """ Show every product through a for loop """
    if len(product_stock) == 0:
        print("No products found in stock.")
    else:
        for key in product_stock:
            print("Product name:",key)
            if product_stock[key]["amount"] == 0:
                print("Product out of stock.")
            else:
                print("Product amount in stock:",product_stock[key]["amount"])
            print("Product price:",product_stock[key]["price"])
            if len(product_stock[key]["price_historic"]) > 1:
                print("All prices product has had:")
                for value in product_stock[key]["price_historic"]:
                    print(value)
            print("Product category:",product_stock[key]["category"])
    enter = input("Press enter to go back to the menu...")
