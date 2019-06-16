# shopping-cart

## Setup:

This project exists in the remote repository: https://github.com/richiebubbs/shopping-cart

## Create and activate a new conda environment:
```sh
conda create -n shopping-env python=3.7 #First time only
conda activate shopping-env
```
## Run the app:
Within the virtual environment, run the app as follows:
```sh
python shopping_cart.py
```

The app will ask the user for a product identifier.  The user can enter as many valid items as she likes.  When done, the user can simply enter "DONE" (all caps) to exit.  The user will be prompted with the following: "Please enter a product identifier (or enter 'done' to exit):"
If an invalid selection is made, an error message will inform the user to try again.

After the user enters "DONE" all the selected items will be displayed along with the price for each item.  The total price will be added with the applicable tax.

