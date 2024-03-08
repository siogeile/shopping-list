#xxxxxxxxxxxxxxxxxx__24_ROWS_HIGH_80_CHAR_WIDE__xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
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
    #gets all the values in the shopping list without the headings row
    shopping_list_data = shopping.col_values(1)

    return shopping_list_data[1:]

shopping_list = shopping_list_items()

def print_shopping_list():
    """
    Prints the shopping list to the terminal
    """
    print("Loading your shopping list...\n")
    print("--- SHOPPING LIST ---\n")
    for item in shopping_list:
        print("- " + item)
    
    print("")

def add_new_items():
    """
    Get item names input from the user
    """
    while True:
        print("")
        print("Add items to your shopping list.")
        print("- Separate items with commas")
        print("- Example: Spinach, Ginger ale, Chocolate\n")

        data_str = input("Add items: \n")
        new_items = data_str.split(",")

        if validate_data(new_items):
            print("Items validated")
            break

    print(f"You have added {new_items} to your list")
    
    return new_items

def validate_data(words):
    """
    Raises ValueError if any input item is empty or too long
    """
    try:
        for word in words:
            if len(str(word)) > 20:
                raise ValueError(
                    "Single items should be less than 20 characters"
                )
            elif not str(word).strip():
                raise ValueError(
                    "Entry invalid.\
                        Please make sure all entries contain \
                            at least one character each"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

# Code copied with edits from Geek Tutorials on YouTube
def main_menu():
    """
    Load a menu that will loop back once the functions in the
    selections complete
    """
    while True:
        print('''

        Select the number of the action that you would like to do:

        1. View Shopping List
        2. Add items to shopping list
        3. View all items
        4. Remove item from shopping list
        5. Check if item is on shopping list
        6. Clear Shopping List
        7. Delete items
        8. Exit''')
        print("")

        selection = input("What would you like to do?: ")
        print("")

        if selection == "1":
            print_shopping_list()
        elif selection == "2":
            add_new_items()
        elif selection == "3":
            pass
        elif selection == "4":
            pass
        elif selection == "5":
            pass
        elif selection == "6":
            pass
        elif selection == "7":
            pass
        elif selection == "8":
            sys.exit()
        else:
            print("You did not make a valid selection")

# MAIN MENU

main_menu()