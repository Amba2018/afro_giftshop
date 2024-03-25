# Settings and credentials to allow access, read and modify data in
# Google Sheets
import gspread
from google.oauth2.service_account import Credentials

# time and sys libraries to add typing effect/delay
import time
import sys

# os library to clear screen
import os

# colorama for text formatting
import colorama
from colorama import Fore, Back, Style

# initialize colorama
colorama.init(autoreset=True)

# Scope for Google IAM auth for API program access
# Guidance for setting up the APIs was provided by the Code Institute's
# course material
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# const for untracked creds file
CREDS = Credentials.from_service_account_file('creds.json')
# const for credentials scope
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# const to allow auth of gspread client within these scoped credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# const for google sgeet
SHEET = GSPREAD_CLIENT.open('afro_giftshop')

# typing effect function with delay effect for print and input
# time.sleep() used as a pause effect with seconds parameter
# clearScreen() to reset screen for new text
def typePrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def typeInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value

def prog_start():
   '''
   Run opening screen for user and gives brief explanation of its use.
   '''
   print('''
   
                                                                             
     .oo  d'b                .oPYo.  o  d'b   o         8                    
    .P 8  8                  8    8     8     8         8                    
   .P  8 o8P  oPYo. .oPYo.   8      o8 o8P   o8P .oPYo. 8oPYo. .oPYo. .oPYo. 
  oPooo8  8   8  `' 8    8   8   oo  8  8     8  Yb..   8    8 8    8 8    8 
 .P    8  8   8     8    8   8    8  8  8     8    'Yb. 8    8 8    8 8    8 
.P     8  8   8     `YooP'   `YooP8  8  8     8  `YooP' 8    8 `YooP' 8YooP' 
..:::::..:..::..:::::.....::::....8 :..:..::::..::.....:..:::..:.....:8 ....:
::::::::::::::::::::::::::::::::::8 ::::::::::::::::::::::::::::::::::8 :::::
::::::::::::::::::::::::::::::::::..::::::::::::::::::::::::::::::::::..:::::

   ''')

def add_sales():
    """
    User adds sales data.
    """
    typePrint("Please enter days sales (6 numbers, separated by commas)... \n")
    data_str = typeInput("Enter sales here: \n")

    sales_data = data_str.split(",")

    typePrint(f"You have entered : {sales_data}\n")
    typeInput("Please confirm: Y or N\n")


def main():
    """
    Menu is displayed with options for user input
    """
    typePrint("Welcome to Afro GiftShop.\n")
    time.sleep(1) 
    print("\n")
    typePrint("Please choose from the menu below.\n")
    time.sleep(1)
    print("\n")
    print("1. Add sales.\n")
    print("2. Check store reserve batch.\n")
    print("3. Check inventory.\n")
    print("4. Update inventory.\n")
    print("5. Calculate profits.\n")
    print("6. Exit.\n")  


    choice = int(typeInput("Enter your choice: \n"))
    if choice == 1:
        add_sales()

prog_start()

main()