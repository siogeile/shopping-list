import gspread
from google.oauth2.service_account import Credentials
import sys
import time


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

# Code copied with edits from Geek Tutorials on YouTube


def main_menu():
    """
    Load a menu that will loop back once the functions in the
    selections complete
    """
    while True:
        clear_screen()
        print('''
        Enter a number to make a selection

        1. View Shopping List
        2. Add items to shopping list
        3. Remove item from shopping list
        4. Exit''')

        time.sleep(.3)
        selection = input("\nWhat would you like to do?:\n ")

        if selection == "1":
            clear_screen()
            print_shopping_list()
        elif selection == "2":
            clear_screen()
            addition = add_new_items()
            update_worksheet(addition, 'shopping')
        elif selection == "3":
            clear_screen()
            deduction = remove_items()
            update_removal(deduction, 'shopping')
        elif selection == "4":
            clear_screen()
            time.sleep(1)
            sprint("See you soon")
            time.sleep(2)
            clear_screen()
            sys.exit()
        else:
            sprint("\nYou did not make a valid selection")

        time.sleep(.05)


def clear_screen():
    """
    Clears the screen using ANSI VT100 codes
    """
    print('\033[H\033[J')
    return


def sprint(str):
    """
    Reduces the speed of text as it appears in the terminal
    """
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)


def return_to_home(action_function):
    while True:
        print("\nDo you want to go back to the main menu?")
        return_home = input("y/n: ").lower()
        if return_home == 'y':
            return
        elif return_home == 'n':
            sprint("We can stay here for now")
        else:
            sprint("You did not make a valid selection")


def shopping_list_items():
    """
    returns the values of the shopping list
    """
    shopping = SHEET.worksheet('shopping').get_all_values()
    shopping_list_data = shopping[-1]

    return shopping_list_data


shopping_list = shopping_list_items()


def print_shopping_list():
    """
    Prints the shopping list to the terminal
    """
    sprint("Loading your shopping list...\n")
    print("--- SHOPPING LIST ---\n")

    # retrieve shopping list updates
    shopping_list = shopping_list_items()

    for item in shopping_list:
        print("- " + item)

    return_to_home(print_shopping_list)


def add_new_items():
    """
    Get item names input from the user
    """
    while True:
        print("\nAdd items to your shopping list.")
        print("- Separate items with commas")
        print("- Example: Spinach, Ginger ale, Chocolate\n")

        data_str = input("Add items: \n")
        new_items = data_str.split(",")

        if validate_data(new_items):
            print("Items validated")
            sprint(f"You have added {new_items} to your list")
            break

    return new_items


def remove_items():
    """
    Get input for items to remove from the user
    """
    while True:
        print("\nRemove items from your shopping list.")
        print("Be careful of the spelling")
        print("- Separate items with commas")
        print("- Example: Spinach, Ginger ale, Chocolate\n")

        data_str = input("Remove items: \n")
        removed_items = data_str.split(",")

        if validate_data(removed_items) and validate_removal(removed_items):
            print("Items located and validated")
            sprint(f"You have removed {removed_items} from your list")
            break

    return removed_items


def validate_data(words):
    """
    Raises ValueError if any input item is empty or too long
    """
    try:
        for word in words:
            if len(str(word)) > 20:
                raise ValueError(
                    "One or more items exceeded 20 characters"
                )
            elif not str(word).strip():
                raise ValueError(
                    "Did you enter an empty value?"
                )
                time.sleep(1)
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        time.sleep(1)
        return False

    return True


def validate_removal(words):
    """
    Raises ValueError if any input item is not on the shopping list
    """
    shopping_list = shopping_list_items()

    try:
        for word in words:
            if word not in shopping_list:
                raise ValueError(f"{word} not found on the shopping list")
            time.sleep(.5)
    except ValueError as e:
        print(f"Invalid removal: {e}, please try again.\n")
        time.sleep(.5)
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receive a list of values to insert into a worksheet
    Update the relevant worksheet with the data provided
    """
    sprint(f"Updating {worksheet} list...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)

    # get existing values in the first row
    existing_values = worksheet_to_update.row_values(1)

    # concatate the existing values with the new items
    updated_values = existing_values + data

    # amend the first row with the updated values
    worksheet_to_update.update([updated_values], '1:1')

    print(f"Your {worksheet} list updated successfully\n")
    time.sleep(1)


def update_removal(data, worksheet):
    """
    Receive a list of values to remove from a worksheet
    Update the relevant worksheet by removing the specified items
    """
    sprint(f"Updating {worksheet} list...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)

    # get existing values in the first row
    existing_values = worksheet_to_update.row_values(1)

    # Create a new list excluding the items to be removed
    updated_values = [
        item for item in worksheet_to_update.row_values(1) if item not in data
        ]

    # get number of values in the list before deductions
    num = len(existing_values)

    # update the same value of cells in the row with empty values
    worksheet_to_update.update([[""] * num], '1:1')

    # Add the new values to the sheet once the data has been cleared
    worksheet_to_update.update([updated_values], '1:1')

    print(f"{worksheet} list updated successfully\n")
    time.sleep(1)

# MAIN MENU


clear_screen()
print("\nWelcome!")
time.sleep(2)
sprint("\nYour shopping list application is loading...")
time.sleep(.5)
main_menu()
