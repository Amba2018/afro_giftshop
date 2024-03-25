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


def clearScreen():
    os.system("clear")

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

def return_main():
    """
    Return to main menu
    """
    while True:
        choice = input("""
                       \n
                       \n
                       \n
                       To return to Main Menu, please enter 'M'.
                       \n
                       """)
        if choice == 'M' or choice == 'm':
            time.sleep(1.5)
            clearScreen()
            main()
            break
        else:
            print("Invalid input, please try again")
            continue


def print_sales():
    """
    Print sales data to terminal
    """
    print('you have reached sales')

    time.sleep(2)
    return_main()

def check_sales():
    """
    Check sales by date and print in terminal
    """
    clearScreen()
    typePrint("Please enter date in the format DD-MM-YYYY... \n")
    data_str = typeInput("Enter date here: \n")
    if len(data_str) == 10:
        try:
            print("Valid Date")
            typePrint(f"You have entered: {data_str}\n")
            while True:
                choice = typeInput("Please confirm: Y or N\n")
                try:
                    if choice == 'Y' or choice == 'y':
                        print_sales()
                        break
                    elif choice == 'N' or choice == 'n':
                        check_sales()
                        break
                    else:
                        print("Invalid input, please try again")
                        continue
                except ValueError:
                    typePrint("Invalid input. Please enter date in format DD-MM-YYYY")
                    clearScreen()
                    time.sleep(.5)
                    check_sales()
        except ValueError:
                print("Invalid Date")
                clearScreen()
                time.sleep(.5)
                check_sales()
    else:
        print("Invalid date format, please try again.")
        time.sleep(2)
        check_sales()

    # date_data = data_str.split(" " + "-" + " " + "-" + " ")
    # typePrint(f"You have entered : {date_data}\n")
    # typeInput("Please confirm: Y or N\n")


def sales_input():
    typePrint("Enter days sales (6 numbers, separated by commas)\n")
    data_str = typeInput("Enter sales here: \n")
    sales_data = data_str.split(",")
    validate_sales(sales_data)
    typePrint(f"You have entered : {data_str}\n")
    typeInput("Please confirm: Y or N\n")


def validate_sales(values):
    """
    Convert string values into integers and raise ValueError if 
    strings cannot be converted into int. Check for 6 values.
    Credit: Code Institute Love Sandwiches project
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"6 values required, you provided {len(values)}"
            )
    except ValueError:
        typePrint(f"Input invalid, please try again.\n")
        sales_input()
        return False

    return True

def sales_input():
    typePrint("Enter days sales (6 numbers, separated by commas)\n")
    data_str = typeInput("Enter sales here: \n")
    sales_data = data_str.split(",")
    validate_sales(sales_data)
    typePrint(f"You have entered : {data_str}\n")
    while True:
        choice = typeInput("Please confirm: Y or N\n")
        if choice == 'Y' or choice == 'y':
            typePrint(f"The sales figures {data_str} have been recorded.\n")
            time.sleep(1)
            print("\n")
            return_main()
            break
        elif choice == 'N' or choice == 'n':
            sales_input()
            break
        else:
            print("Invalid input, please try again")
            continue


def rec_sales():
    """
    Record daily sales
    """
    typePrint("Please enter date in the format DD-MM-YYYY... \n")
    data_str = typeInput("Enter date here: \n")
    if len(data_str) == 10:
        try:
            print("Valid Date")
            typePrint(f"You have entered: {data_str}\n")
            while True:
                choice = typeInput("Please confirm: Y or N\n")
                try:
                    if choice == 'Y' or choice == 'y':
                        print_sales()
                        sales_input()
                        break
                    elif choice == 'N' or choice == 'n':
                        rec_sales()
                        break
                    else:
                        print("Invalid input, please try again")
                        continue
                except ValueError:
                    typePrint("Invalid input. Please enter date in format DD-MM-YYYY")
                    clearScreen()
                    time.sleep(.5)
                    rec_sales()
        except ValueError:
                print("Invalid Date")
                clearScreen()
                time.sleep(.5)
                rec_sales()
    else:
        print("Invalid date format, please try again.")
        time.sleep(2)
        rec_sales()

def day_sales():
    """
    Go to sales menu
    """
    clearScreen()
    typePrint("Sales Menu")
    time.sleep(1)
    while True:
        print("""
            1. Check sales
            2. Add days sales
            """)
        try:
            choice = int(typeInput("Please choose from menu...\n"))
            if choice == 1:
                check_sales()
                break
            elif choice == 2:
                rec_sales()
                break
        except ValueError:
            typePrint("Invalid input. Please choose a numbered menu item.")
            time.sleep(1.5)
            clearScreen()
            continue
def print_batch():
    """
    Print batch numbers from date input
    """
    print("You have reached print batch")
    time.sleep(1)
    return_main()


def Update_batch():
    """
    User adds store reserve batch
    """
    typePrint("Please enter store reserve batch (6 numbers, separated by commas)... \n")
    data_str = typeInput("Enter batch here: \n")

    batch_data = data_str.split(",")

    typePrint(f"You have entered : {batch_data}\n")
    typeInput("Please confirm: Y or N\n")
    

def check_invt():
    """
    Pull inventory data from google sheet-inventory
    """
    typePrint("Checking inventory levels...\n")
    time.sleep(1)
    typePrint("Current inventory levels are: \n")

def Update_invt():
    """
    User adds needed day inventory
    """
    typePrint("Please enter day inventory (6 numbers, separated by commas)... \n")
    data_str = typeInput("Enter batch here: \n")

    invt_data = data_str.split(",")

    typePrint(f"You have entered : {invt_data}\n")
    typeInput("Please confirm: Y or N\n")

def cal_pro()


def exit():
    """
    return to program start screen
    """
    typePrint("Returning to program start...")
    time.sleep(2)
    print("\n")
    print("\n")


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
    print("2. Update store reserve batch.\n")
    print("3. Check inventory.\n")
    print("4. Update inventory.\n")
    print("5. Calculate profits.\n")
    print("6. Exit.\n")  

    print('''
        *******************************************************
        * ALERT: All Set for the day.                     *
        *******************************************************
        ''')
    while True:
        try:
            choice = int(typeInput("Enter your choice: \n"))
            if choice == 1:
                day_sales()
            elif choice == 2:
                Update_batch()
            elif choice == 3:
                check_invt()
            elif choice == 4:
                Update_invt()
            elif choice == 5:
                calc_pro()
            elif choice == 6:
                exit()
        except ValueError:
            typePrint("Invalid input. Please choose a numbered menu item...")
            time.sleep(1.5)
            clearScreen()
            main()


prog_start()

main()