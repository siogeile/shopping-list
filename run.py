import gspread
from google.oauth2.service_account import Credentials
import sys

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('shopping-list')

# FUNCTIONS

def shopping_list_items():
    """
    returns the values of the shopping list
    """
    shopping = SHEET.worksheet('shopping')
    #gets all the values in the first column of the 'shopping' sheet
    shopping_list_data = shopping.col_values(1)

    return shopping_list_data[1:]

shopping_list = shopping_list_items()

def print_shopping_list():
    """
    Prints the shopping list to the terminal
    """
    print("Loading your shopping list...\n")
    print("Shopping List:")
    for item in shopping_list:
        print(item)
    
    print("")

print_shopping_list()

def add_new_items():
    """
    Get item names input from the user
    """
    print("Add items to your shopping list.")
    print("- Separate items with commas")
    print("- Example: Spinach, Ginger ale, Chocolate\n")

    data_str = input("Add items to your list here: ")
    new_items = data_str.split(",")
    print(f"You have added {new_items} to your list")

add_new_items()