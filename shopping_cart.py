# shopping_cart.py

#from pprint import pprint
import pandas as pd
import datetime


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

products_list_csv = pd.read_csv('/Users/richiebubbs/Downloads/GitHub/shopping-cart/data/products.csv')
acceptable_inputs = [i["id"] for i in products]
#print(acceptable_inputs)

#I constructed this while loop with help from https://realpython.com/python-while-loop/

a = False
while not a:
    print("Please enter a product identifier (or enter 'done' to exit): ")
    x = input()
    if x != "done" and int(x) in acceptable_inputs:
       a = False
    elif x == "done":
        a = True
    else:
        print("I'm sorry, that is not a valid selection, please try again")


print("--------------------------------------")
print("RichieBubbs Grocery Emporium")
print("WWW.RICHIEBUBBS-GROCERY-EMPORIUM.COM")
print("--------------------------------------")
# for date time I got some help from https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
now = datetime.datetime.now()
print("CHECKOUT AT: ", now)
print("--------------------------------------")
print("SELECTED PRODUCTS:")
#> ---------------------------------
#> GREEN FOODS GROCERY
#> WWW.GREEN-FOODS-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: 2019-06-06 11:31 AM
#> ---------------------------------
#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Dry Nose Oil ($21.99)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Mint Chocolate Flavored Syrup ($4.50)
#>  ... Chocolate Fudge Layer Cake ($18.50)
#> ---------------------------------
#> SUBTOTAL: $61.24
#> TAX: $5.35
#> TOTAL: $66.59
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------

#print(products_list_csv)
