# shopping_cart.py

#from pprint import pprint
import pandas as pd
import datetime
import time



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
acceptable_inputs = [str(i["id"]) for i in products]
selected_products = []
#print(acceptable_inputs)

#I constructed this while loop with help from https://realpython.com/python-while-loop/
# I reconstructed the loop with some help form your screencast when I got stuck... 
#https://www.youtube.com/watch?v=3BaGb-1cIr0&feature=youtu.be

total_price = 0
selected_ids = []
a = False
while not a:
    print("Please enter a product identifier (or enter 'DONE' to exit): ")
    x = input()
    if x != "DONE" and x in acceptable_inputs:
       a = False
       #matching_products = [p for p in products if str(p["id"])==x]
       #matching_product = matching_products[0]
       #total_price = total_price + matching_product["price"]
       selected_ids.append(x)
       #print("..." + matching_product["name"] + "(" + str(matching_product["price"])+ ")")
       #print(type(x))
    elif x == "DONE":
        a = True
    else:
        print("I'm sorry, that is not a valid selection, please try again")



#print("Total Price: ", total_price)

#print(selected_products) i did this to make sure that the list was being properly appended

#breakpoint()
time.sleep(1)
print("                                      ")
print("Here is your receipt")
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
print("                                      ")
print("--------------------------------------")
print("                                      ")
print("RichieBubbs Grocery Emporium")
print("WWW.RICHIEBUBBS-GROCERY-EMPORIUM.COM")
print("                                      ")
print("--------------------------------------")
# for date time I got some help from https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
# and for formatting: https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
# https://stackoverflow.com/questions/31487732/simple-way-to-drop-milliseconds-from-python-datetime-datetime-object

now = datetime.datetime.now().replace(microsecond=0)
print("CHECKOUT AT: ", now)
print("                                      ")
print("--------------------------------------")
print("                                      ")
print("SELECTED PRODUCTS:")
for y in selected_ids:
    matching_products = [p for p in products if str(p["id"])==y]
    matching_product = matching_products[0]
    #price_usd = "{0:.2f}".format(matching_product["price"])
    price_usd = "{0:.2f}".format(matching_product["price"])    
    total_price = total_price + matching_product["price"]
    ttl_price_usd = "{0:.2f}".format(total_price)
    print("..." + matching_product["name"] + "($" + str(price_usd)+ ")")
    tax = total_price * 0.08875
    tax_price_usd = "{0:.2f}".format(tax)
    grand_ttl = total_price + tax
    grand_ttl_price_usd = "{0:.2f}".format(grand_ttl)
    
print("--------------------------------------")
print("                                      ")
print("SUBTOTAL: $" + str(ttl_price_usd))
print("TAX: $" + str(tax_price_usd))
print("TOTAL: $" + str(grand_ttl_price_usd))
print("                                      ")
print("--------------------------------------")
print("THANK YOU, COME AGAIN!")
print("--------------------------------------")

#for y in selected_products:
#    matching_products_name = [p["name"] for p in products if p["id"]==y]
#    matching_products_price =[p['price'] for p in products if p['id']==y]





    


#print(final_product_selection, final_product_price)


#for p in selected_products:
#    print("..." + products["id"] == p)
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
