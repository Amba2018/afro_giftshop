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

ingInvt = {
   "T-Shit": "500",
    "Cup":"650",
    "Book":"750",
    "Map":"250",
    "Picture":"850",
    "Pen":"750",
    "Pencil":"750",
    "Cocoa":"150",
    "Bracelets":"320"                   
}


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
                       To return to Main Menu, please enter 'M'.
                       \n
                       """)
        if choice == 'M' or choice == 'm':
            time.sleep(1)
            clearScreen()
            main()
            break
        else:
            print("Invalid input, please try again")
            continue


def print_sales():
    """
    Print sales data by date to terminal
    """
    clearScreen()
    sales_sheet = SHEET.worksheet("sales").get_all_values()
    typePrint("** Sales figures by date **\n")
    print("""
                       - SHOP LIST -
                    T-Shit       Books
                    Pens         Bracelets
                    Cocoa        Cups\n
          """)
    # \t to format and display sales data from gsheet into terminal
    print("****************************************************************\n")
    for row in sales_sheet:
        print('\t'.join(row))
    print("\n")
    print("****************************************************************\n")  
    time.sleep(2)
    return_main()


def check_sales():
    """
    Check sales by date and print in terminal
    """
    clearScreen()
    typePrint("Please enter date in the format DD-MM-YYYY.\n")
    sales_date_str = typeInput("Enter date here: \n")
    if len(sales_date_str) == 10:
        try:
            typePrint(f"You have entered: {sales_date_str}\n")
while True:
    choice = typeInput("Please confirm: Y or N.\n")
    try:
        if choice == 'Y' or choice == 'y':
            sales_sheet = SHEET.worksheet("sales").get_all_values()
            for row in sales_sheet:
                print('\t'.join(row))                    
            break
        elif choice == 'N' or choice == 'n':
            check_sales()
            break
        else:
            print("Invalid input, please try again.")
            continue
    except ValueError:
        typePrint("Invalid input. Please enter date in format DD-MM-YYYY.")
        clearScreen()
        time.sleep(.5)
        check_sales()
        
   
def validate_sales(values):
    """
    Convert string values into integers and raise ValueError if 
    strings cannot be converted into int. Check for 6 values.
    Credit: Code Institute Love Sandwiches project
    """
    try:
        [int(value) for value in values]
        if len(values) != 9:
            raise ValueError(
                f"6 values required, you provided {len(values)}"
            )
    except ValueError:
        typePrint(f"Input invalid, please try again.\n")
        sales_input()
        return False
    return True


def sales_input():
    typePrint("Enter date & sales figures "
              "(DD,MM,YYYY, sales figures, separated by commas).\n")
    sales_figs = typeInput("Enter sales here: \n")
    sales_data = sales_figs.split(",")
    validate_sales(sales_data)
    sales_str = ','.join(sales_data)
    typePrint(f"You have entered : {sales_str}\n")
    while True:
        choice = typeInput("Please confirm: Y or N.\n")
        if choice == 'Y' or choice == 'y':
            sales_sheet = SHEET.worksheet("sales")
            sales_sheet.append_row(sales_data)
            typePrint(f"The sales figures have been recorded.\n")
            time.sleep(1)
            print("\n")
            return_main()
            break
        elif choice == 'N' or choice == 'n':
            sales_input()
            break
        else:
            print("Invalid input, please try again.")
            continue
'''    
def rec_sales():
    """
    Record daily sales
    """
    typePrint("Please enter date in the format DD-MM-YYYY.\n")
    rec_date = typeInput("Enter date here: \n")
    #gs_date_rec = datetime.strftime(rec_date, '%d/%m/%Y')
    if len(rec_date) == 10:
        try:
            typePrint(f"You have entered: {rec_date}\n")
            while True:
                choice = typeInput("Please confirm: Y or N.\n")
                try:
                    if choice == 'Y' or choice == 'y':
                        # sales_date = SHEET.worksheet("sales")
                        # sales_date.insert_rows(rec_date)
                        sales_input()
                        break
                    elif choice == 'N' or choice == 'n':
                        rec_sales()
                        break
                    else:
                        print("Invalid input, please try again.")
                        continue
                except ValueError:
                    typePrint("Invalid input. Enter date in format DD-MM-YYYY.")
                    clearScreen()
                    time.sleep(.5)
                    rec_sales()
        except ValueError:
                print("Invalid Date.")
                clearScreen()
                time.sleep(.5)
                rec_sales()
    else:
        print("Invalid date format, please try again.")
        time.sleep(2)
        rec_sales()
'''
    
def day_sales():
    """
    Go to sales menu
    """
    clearScreen()
    print("** Sales Menu **")
    while True:
        print("""
            1. Check sales by date.
            2. Add days sales.
            """)
        try:
            choice = int(typeInput("Please choose from menu.\n"))
            if choice == 1:
                check_sales()
                break
            elif choice == 2:
                sales_input()
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
    print("You have reached print batch.")
    time.sleep(1)
    return_main()

def check_batch():
    """
    Pull date of day batch nums data from google sheets-batch
    """
    clearScreen()
    time.sleep(0.5)
    typePrint("Please enter date in format DD-MM-YYYY.\n")
    data_str = typeInput("Enter date here: \n")
    if len(data_str) == 10:
        try:
            typePrint(f"You have entered: {data_str}\n")
            while True:
                choice = typeInput("Please confirm: Y or N\n")
                try:
                    if choice == 'Y' or choice == 'y':
                        print_batch()
                        break
                    elif choice == 'N' or choice == 'n':
                        check_batch()
                        break
                    else:
                        print("Invalid input, please try again")
                        continue
                except ValueError:
                    typePrint("Invalid input. Please enter date in format DD-MM-YYYY.")
                    clearScreen()
                    time.sleep(.5)
                    check_batch()
        except ValueError:
                print("Invalid Date")
                clearScreen()
                time.sleep(.5)
                check_batch()
    else:
        print("Invalid date format, please try again.")
        time.sleep(2)
        check_batch()


def check_invt():
    """
    Pull inventory data from google sheet-inventory
    Print list vertically
    """
    typePrint("Checking inventory levels...")
    time.sleep(1)
    clearScreen()
    typePrint(f"** Current inventory levels are: **\n")
    print("\n")
    for key, value in ingInvt.items():
        print('- ', key, ':', value)
    print("\n")
    while True:
        user_input = input("Would you like to update an item? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            clearScreen()
            update_invt()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()  
            break 
    time.sleep(1)
    return_main()


def user_update():
    while True:
        ing_name = input("Please choose ingredient from the list: \n")
        if ing_name in ingInvt:
            updated_value = input("Enter new value for ingredient: \n")
            ingInvt[ing_name] = updated_value
            print(f"{ing_name} updated to {updated_value}\n")
            time.sleep(1.5)
            break
        else:
            print(f"{ing_name} is not in this list.\n")
            continue


def print_invt_ws():
    """
    Print inventory levels to google sheet when updated
    """
    invt_sheet = SHEET.worksheet("inventory")
    # convert dictionary to list of lists
    invt_data = [value for value in ingInvt.items()]
    invt_sheet.append_row(invt_data)


def update_invt():
    """
    Allow user to add additional amounts to increase
    inventory levels.
    """
    clearScreen()
    typePrint("** Update inventory levels. **")
    print("\n")
    typePrint("** Current Inventory levels are: **")
    print("\n")
    time.sleep(1)
    for key, value in ingInvt.items():
        print('- ', key, ':', value)
    print("\n")
    user_update()
    print_invt_ws()
    clearScreen()
    typePrint("** Updated inventory levels are: **\n")
    print("\n")
    for key, value in ingInvt.items():
        print('- ', key, ':', value)
    print("\n")
    time.sleep(1)
    return_main()


def calc_pro():
    """
    Calculate daily profits by subtracting total batch cost from
    daily sales figure. Append profit worksheet to include days profits.
    """
    typePrint("Please enter date in format DD-MM-YYYY...\n")
    data_str = typeInput("Enter date here: \n")
    time.sleep(1)
    return_main()


def exit():
    """
    return to program start screen
    """
    typePrint("Returning to program start...")
    time.sleep(2)
    print("\n")
    print("\n")
    clearScreen()


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

   
    while True:
        try:
            choice = int(typeInput("Enter your choice: \n"))
            if choice == 1:
                day_sales()
            elif choice == 2:
                check_batch()
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
            time.sleep(1)
            continue


prog_start()

main()