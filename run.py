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
        typePrint("Input invalid, please try again.\n")
        sales_input()
        return False
    return True


def sales_input():
    """
    Allow user input of date and sales figures to be entered
    and used to update sales worksheet.
    """
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
            typePrint("The sales figures have been recorded.\n")
            time.sleep(1)
            print("\n")
            day_sales()
            break
        elif choice == 'N' or choice == 'n':
            sales_input()
            break
        else:
            print("Invalid input, please try again.")
            continue


def clear_sales():
    """
    Clear all sales data from sales worksheet
    """
    clearScreen()
    typePrint("*** CLEAR ALL SALES DATA ***")
    print("\n")
    choice = typeInput("To clear all Sales Data please enter 'CLEAR DATA'.\n")
    if choice == 'CLEAR DATA':
        typePrint("Please confirm Y or N to clear all data:\n")
        final_c = typeInput("Enter choice here: \n")
        if final_c == 'Y' or final_c == 'y':
            sales_sheet = SHEET.worksheet("sales")
            sales_sheet.batch_clear(["A2:J10000"])
            time.sleep(1)
            typePrint("Sales sheet successfully cleared.")
            day_sales()
        elif final_c == 'N' or final_c == 'n':
            typePrint("Abort data delete.")
            day_sales()
        else:
            typePrint("Invalid input. Returning to Sales menu.")
            time.sleep(1.5)
            day_sales()
    else:
        typePrint("Invalid input.\n")
        check_c = typeInput("Please enter 'C' to continue or 'X' to exit.\n")
        if check_c == 'C' or check_c == 'c':
            clear_sales()
        elif check_c == 'X' or check_c == 'x':
            day_sales()
        else:
            typePrint("Invalid input. Returning to main menu.")
            time.sleep(1.5)
            return_main()


def day_sales():
    """
    Go to sales menu
    """
    clearScreen()
    print("** SALES MENU **")
    while True:
        print("""
            1. View sales data\n
            2. Add days sales\n
            3. Clear data\n
            4. Main menu
            """)
        try:
            choice = int(typeInput("Please choose from menu.\n"))
            if choice == 1:
                print_sales()
                break
            elif choice == 2:
                sales_input()
                break
            elif choice == 3:
                clear_sales()
                break
            elif choice == 4:
                return_main()
                break
        except ValueError:
            typePrint("Invalid input. Please choose a numbered menu item.")
            time.sleep(1.5)
            clearScreen()
            continue

    
def user_update_batch():
    """
    Allow user input to update next day batch levels
    """
    batch_sheet = SHEET.worksheet("batch")
    records = batch_sheet.get_all_records()
    while True:
        item_choice = input("Enter item as displayed above: \n")
        record_found = False
        for record in records:
            if record["item"] == item_choice:
                record_found = True
                while True:
                    try:
                        update_q = int(input(f"Enter value for {item_choice}:\n"))
                        record["Quantity"] = update_q
                        # update with new data to inventory sheet
                        for i, record in enumerate(records, start=2):
                            batch_sheet.update_cell(i,2,record["Quantity"]) 
                        typePrint("Inventory successfully updated.\n")
                        choice = input("Update another items? Enter Y or N.\n")
                        if choice == 'Y' or choice == 'y':
                            user_update_batch()
                        elif choice == 'N' or choice == 'n':
                            return_main()
                    except ValueError:
                        typePrint("Value must be numerical. Try again.\n")
                        continue
                    else:
                        return update_q
        if not record_found:
            print("Item not found in inventory.\n")
            continue


def check_batch():
    """
    Pull batch data from batch google sheet and allow
    user to update quantity and amend worksheet
    """
    typePrint("Fetching batch numbers for today...")
    time.sleep(1)
    clearScreen()
    print("\n")
    typePrint(f"** TODAYS BATCH NUMBERS **")
    print("\n")
    batch_sheet = SHEET.worksheet("batch")
    batch_list = batch_sheet.col_values(1)
    q_list = batch_sheet.col_values(2)
    # list/zip for parallel iteration
    pairs = list(zip(batch_list, q_list))
    for pair in pairs:
        print('- ', pair[0], ': ', pair[1])
    print("\n")
    typePrint("ATTN: Batch = 12 cupcakes.\n")
    print("\n")
    while True:
        user_input = input("Would you like to update batches? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            user_update_batch()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()
            break
    time.sleep(1)
    return_main()


def user_update_ing():
    """
    Allow user input to update inventory levels
    """
    invt_sheet = SHEET.worksheet("inventory")
    records = invt_sheet.get_all_records()
    while True:
        ing_choice = input("Enter item name as displayed above: \n")
        record_found = False
        for record in records:
            if record["Item"] == ing_choice:
                record_found = True
                while True:
                    try:
                        update_q = int(input(f"Enter value for {ing_choice}:\n"))
                        record["Quantity"] = update_q
                        # update with new data to inventory sheet
                        for i, record in enumerate(records, start=2):
                            invt_sheet.update_cell(i,2,record["Quantity"]) 
                        typePrint("Inventory successfully updated.\n")
                        choice = input("Update another item? Enter Y or N.\n")
                        if choice == 'Y' or choice == 'y':
                            user_update_ing()
                        elif choice == 'N' or choice == 'n':
                            return_main()
                    except ValueError:
                        typePrint("Value must be numerical. Try again.\n")
                        continue
                    else:
                        return update_q
        if not record_found:
            print("Item not found in inventory.\n")
            continue
               

def check_invt():
    """
    Pull inventory data from inventory google sheet and allow
    user to update levels and amend worksheet
    """
    typePrint("Checking inventory levels...")
    time.sleep(1)
    clearScreen()
    print("\n")
    typePrint(f"** CURRENT INVENTORY LEVELS **")
    print("\n")
    invt_sheet = SHEET.worksheet("inventory")
    ing_list = invt_sheet.col_values(1)
    q_list = invt_sheet.col_values(2)
    # list/zip for parallel iteration
    pairs = list(zip(ing_list, q_list))
    for pair in pairs:
        print('- ', pair[0], ': ', pair[1])
    print("\n")
    while True:
        user_input = input("Would you like to update an item? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            user_update_ing()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()
            break
    time.sleep(1)
    return_main()


def calc_pro():
    """
    Calculate daily profits by subtracting total batch cost from
    daily sales figure. Append profit worksheet to include days profits.
    """
    typePrint("Please enter date in format DD-MM-YYYY.\n")
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
    prog_start()
    main()


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