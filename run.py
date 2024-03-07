import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('shopping-list')

shopping = SHEET.worksheet('shopping')

def add_new_items():
    """
    Get item names input from the user
    """
    print("Add items to your shopping list.")
    print("Separate items with commas")
    print("Example: Spinach, Ginger ale, Chocolate\n")

    data_str = input("Add items to your list here: ")
    new_items = data_str.split(",")
    print(f"You have added {new_items} to your list")

add_new_items()