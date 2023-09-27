# evaluation_work_otavio_andrey

# Welcome to our College Project: Stock Management Software for a Store

This software is designed to facilitate the management of products available in the stock center of a store. It provides information on product availability, price, category, amount sold, profit, generates sales reports and even keeps a changelog of stock modifications!

On this readme we'll see a complete breakthrough of the code.

The program is divided in 5 distinct parts, each one doing a part of the code, they're: main.py, menu.py, sales.py, stock.py and historic.py.

##main.py

This is where the program is first initialized and contains important parts of the software, such as the declaration of the necessary variables, lists and dictionaries. The program's functionalities are called here from the many modules we will get into now.

##menu.py
This is where the menu was coded, it contains the 9 option that will call the functionalities of the program on the start_program function on main.py: 
1 - Add a product.
2 - Alter product price
3 - Exclude a product.
4 - Changelog.
5 - Search a product.
6 - Search a category.
7 - View all products.
8 - Sell a product.
9 - Show sales report.
If the user types any other number the program will close.

##sales.py
This is where sales transactions are processed. It prompts the user to input the product's name and quantity to be sold. After the transaction is completed, it adds the total profit generated from the product sale to the sales report along with the other informed variables. It also immediately updates the new quantity in stock of the product.

##stock.py
It manages the overall stock of the store, allowing you to perform the following actions: add products, update product prices, remove products from the stock, search for a product by its name or view all products of a category and view the entire product inventory available. It does this through the multiple functions present in the module.

##historic.py
The final part of this powerful code, that includes the tracking of: additions, modifications, removals, sales and even the time they are made! Here, the changelog and sales report are gradually formed as modifications to stock and sales, respectively, are made. You can also access either of these in this very module.

Feel free to look up the code yourself! 
And most importantly, have a good day!

##WHO MADE THIS:
Andrey Peil [github: AndreyPeil > https://github.com/AndreyPeil]
Otávio Ferreira [github: otaviof3 > https://github.com/otaviof3]

                                            //Trabalho de Laboratório de Algoritmos 2//
                                      Sistemas de Informação, Antonio Meneghetti Faculdade, 2023




