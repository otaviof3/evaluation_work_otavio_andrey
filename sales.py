""" Sales module contains a function for selling products """
import historic
def sell_a_product(product_stock,sales_report,sale_count):
    """ The function for selling a product, does the math and calls the historic module for the sales report function, it also checks if the amount sold is higher than the current amount, then it asks if you want to sell the maximum possible """
    if len(product_stock) == 0:
        print("No products found in stock.")
        enter = input("Press enter to go back to the menu...")
        return product_stock,sales_report,sale_count
    else:
        while True:
            name = input("Name of the product to sell: ").capitalize()
            if name not in product_stock:
                print("Error! Product not found.")
            else:
                break
        if product_stock[name]["amount"] == 0:
            print("Product out of stock!")
            enter = input("Press enter to go back to the menu...")
            return product_stock,sales_report,sale_count
        while True:
            amount_sold = input("Amount to sell: ")
            try:
                amount_sold = int(amount_sold)
                if amount_sold <= 0:
                    print("Error! Type a value higher than 0.")
                else:
                    break
            except:
                print("Error! Type a valid amount!")
        if amount_sold > product_stock[name]["amount"]:
            print("Cannot sell more than the amount available!")   
            sell_option = input("Do you want to sell the maximum amount possible? (Type Y if you do): ").capitalize()
            if sell_option == "Y":
                amount_sold = product_stock[name]["amount"]
                product_stock[name]["amount"] -= amount_sold
                profit = amount_sold * product_stock[name]["price"]
                sales_report,sale_count = historic.edit_sales_report(sales_report,sale_count,name,amount_sold,profit)
                enter = input("Press enter to go back to the menu...")
                return product_stock,sales_report,sale_count
            else:
                enter = input("Press enter to go back to the menu...")
                return product_stock,sales_report,sale_count
        else:
            product_stock[name]["amount"] -= amount_sold
            profit = amount_sold * product_stock[name]["price"]
            sales_report,sale_count = historic.edit_sales_report(sales_report,sale_count,name,amount_sold,profit)
            enter = input("Press enter to go back to the menu...")
            return product_stock,sales_report,sale_count
