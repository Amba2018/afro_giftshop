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
    "Cup": "650",
    "Book": "750",
    "Map": "250",
    "Picture": "850",
    "Pen": "750",
    "Pencil": "750",
    "Cocoa": "150",
    "Bracelets": "320"    
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
   Run opening screen for user and display menu options for user.
   '''
   print("\n")
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
        print("\n")
        choice = typeInput("To return to Main Menu, please enter 'M'.\n")
        if choice == 'M' or choice == 'm':
            time.sleep(1.5)
            clearScreen()
            main()
            break
        else:
            print(Fore.RED + "Invalid input, please try again.")
            continue


def print_sales():
    """
    Print sales data by date to terminal
    """
    clearScreen()
    sales_sheet = SHEET.worksheet("sales").get_all_values()
    print(Back.MAGENTA + Fore.WHITE + "*** SALES FIGURES BY DATE ***\n")
    # \t to format and display sales data from gsheet into terminal
    print("****************************************************************\n")
    for row in sales_sheet:
        print('\t'.join(row))
    print("\n")
    print("****************************************************************\n")
    print("\n")
    if len(sales_sheet) == 0:
        print(Fore.YELLOW + "No Sales Data available.\n")
    while True:
        choice = typeInput("To return to Sales Menu, please enter 'S'.\n")
        if choice == 'S' or choice == 's':
            time.sleep(2)
            clearScreen()
            day_sales()
            break
        else:
            print(Fore.RED + "Invalid input, please try again.")
            continue


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
        print(Fore.RED + "Input invalid, please try again.\n")
        sales_input()
        return False
    return True


def sales_input():
    """
    Allow user input of date and sales figures to be entered
    and used to update sales worksheet.
    """
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + "*** SALES INPUT ***\n")
    typePrint("Enter date & abbreviated shop items (max 4 letters)\n")
    typePrint("(DD,MM,YYYY, 6 souvenirs, separated by commas).\n")
    sales_figs = input(Fore.YELLOW + "Enter here: \n")
    sales_data = sales_figs.split(",")
    sales_str = ','.join(sales_data)
    typePrint("Enter date & sales numbers\n")
    typePrint("(DD,MM,YYYY, six sales numbers, separated by commas).\n")
    sales_nums = input(Fore.YELLOW + "Enter here: \n")
    sales_num_data = sales_nums.split(",")
    validate_sales(sales_num_data)
    sales_num_str = ','.join(sales_num_data)
    print(Fore.GREEN + f"You have entered : {sales_str}\n")
    print(Fore.GREEN + f"You have entered : {sales_num_str}\n")
    while True:
        choice = typeInput("Please confirm: Y or N.\n")
        if choice == 'Y' or choice == 'y':
            sales_sheet = SHEET.worksheet("sales")
            sales_sheet.append_row(sales_data)
            sales_sheet.append_row(sales_num_data)
            typePrint("The sales figures have been recorded.\n")
            time.sleep(2)
            print("\n")
            day_sales()
            break
        elif choice == 'N' or choice == 'n':
            sales_input()
            break
        else:
            print(Fore.RED + "Invalid input, please try again.")
            time.sleep(1)
            continue


def clear_sales():
    """
    Clear all sales data from sales worksheet
    """
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + "*** CLEAR ALL SALES DATA ***\n")
    choice = typeInput("To clear all Sales Data please enter 'CLEAR DATA'.\n")
    if choice == 'CLEAR DATA':
        typePrint("Please confirm Y or N to clear all data:\n")
        final_c = typeInput("Enter choice here: \n")
        if final_c == 'Y' or final_c == 'y':
            sales_sheet = SHEET.worksheet("sales")
            # Clear a certain range
            sales_sheet.clear()
            time.sleep(1)
            print(Fore.GREEN + "Sales sheet successfully cleared.")
            day_sales()
        elif final_c == 'N' or final_c == 'n':
            print(Fore.YELLOW + "Abort data delete.")
            day_sales()
        else:
            print(Fore.RED + "Invalid input. Returning to Sales menu.")
            time.sleep(1.5)
            day_sales()
    else:
        print(Fore.RED + "Invalid input.\n")
        check_c = typeInput("Please enter 'C' to continue or 'X' to exit.\n")
        if check_c == 'C' or check_c == 'c':
            clear_sales()
        elif check_c == 'X' or check_c == 'x':
            day_sales()
        else:
            print(Fore.RED + "Invalid input. Returning to main menu.")
            time.sleep(1.5)
            return_main()


def day_sales():
    """
    Go to sales menu
    """
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + "*** SALES MENU ***")
    while True:
        print(Fore.CYAN + """
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
                clearScreen()
                main()
                break
        except ValueError:
            typePrint("Invalid input. Please choose a numbered menu item.")
            time.sleep(1.5)
            clearScreen()
            continue


def return_batch_menu():
    """
    Print updated batch number data for user and
    provide input choices
    """
    batch_sheet = SHEET.worksheet("batch")
    batch_list = batch_sheet.col_values(1)
    q_list = batch_sheet.col_values(2)
    # list/zip for parallel iteration
    pairs = list(zip(batch_list, q_list))
    for pair in pairs:
        print(Fore.CYAN + '- ', pair[0], Fore.CYAN + ': ', pair[1])
    print("\n")
    print(Fore.YELLOW + "Thank You very much for your service.\n")
    while True:
        user_input = input("Would you like to update batches? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            print("\n")
            batch_options()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()
            break


def add_batch_item():
    """
    Add new batch item and quantity and update Google Sheet.
    """
    batch_sheet = SHEET.worksheet("batch")
    new_batch = input("Enter a new batch item to record (eg: Necklace): \n")
    new_batch_q = input("Enter new batch quantity"
                        " (numerical value only): \n")
    rows_used = len(batch_sheet.col_values(1))
    if rows_used < 7:
        batch_sheet.append_row([new_batch, new_batch_q])
        print(Fore.GREEN + "Batch records successfully updated.\n")
        return_batch_menu()
    else:
        print(Fore.YELLOW + "Sorry, Batch records full."
                            " Max 6 batch item types.\n")
        time.sleep(2)
        return_batch_menu()


def change_batch_item():
    """
    Change item name in batch record and update Google Sheet.
    """
    batch_sheet = SHEET.worksheet("batch")
    batch_o = input("Enter batch name as displayed above: \n")
    batch_n = input("Enter the new batch item: \n")
    values = batch_sheet.col_values(1)
    for i, value in enumerate(values):
        if value == batch_o:
            batch_sheet.update_cell(i+1, 1, batch_n)
    print(Fore.GREEN + "Batch records successfully updated.\n")
    return_batch_menu()


def clear_batch_item():
    """
    Clear batch item completely from records
    """
    batch_sheet = SHEET.worksheet("batch")
    batch_del = input("Enter batch name as displayed above: \n")
    cells_needed = batch_sheet.findall(batch_del, in_column=1)
    rows_to_clear = [cell.row for cell in cells_needed]
    for row in rows_to_clear:
        batch_sheet.delete_rows(row)
    print(Fore.GREEN + "Records updated successfully.\n")
    return_batch_menu()


def user_update_batch():
    """
    Allow user input to update next day batch levels
    """
    batch_sheet = SHEET.worksheet("batch")
    records = batch_sheet.get_all_records()
    while True:
        item = input("Enter item as displayed above: \n")
        record_found = False
        for record in records:
            if record["Items"] == item:
                record_found = True
                while True:
                    try:
                        update_q = int(input(f"Enter value for {item}:\n"))
                        record["Quantity"] = update_q
                        # update with new data to inventory sheet
                        for i, record in enumerate(records, start=2):
                            batch_sheet.update_cell(i, 2, record["Quantity"])
                        print(Fore.GREEN + "Batches successfully updated.\n")
                        batch_sheet = SHEET.worksheet("batch")
                        batch_list = batch_sheet.col_values(1)
                        q_list = batch_sheet.col_values(2)
                        # list/zip for parallel iteration
                        pairs = list(zip(batch_list, q_list))
                        for pair in pairs:
                            print(Fore.CYAN + '- ', pair[0],
                                  Fore.CYAN + ': ', pair[1])
                        print("\n")
                        print(Fore.YELLOW + "Thank you for your service.\n")
                        choice = input("Update another item?"
                                       " Enter Y or N.\n")
                        if choice == 'Y' or choice == 'y':
                            return_batch_menu()
                        elif choice == 'N' or choice == 'n':
                            return_main()
                    except ValueError:
                        print(Fore.RED + "Value must be numerical.\n")
                        continue
                    else:
                        return update_q
        if not record_found:
            print(Fore.RED + "Item not found in inventory.\n")
            continue


def batch_options():
    """
    Menu to choose between adding new batch item, changing batch name
    or updating quantity.
    """
    print(Back.MAGENTA + Fore.WHITE + "*** BATCH MENU ***")
    print("\n")
    print(Fore.CYAN + "1. Add new batch item\n")
    print(Fore.CYAN + "2. Change batch item name\n")
    print(Fore.CYAN + "3. Update batch number\n")
    print(Fore.CYAN + "4. Clear batch item\n")
    print(Fore.CYAN + "5. Return to main menu\n")
    while True:
        try:
            choice = int(input("Please choose from the menu: \n"))
            if choice == 1:
                add_batch_item()
                break
            elif choice == 2:
                change_batch_item()
                break
            elif choice == 3:
                user_update_batch()
                break
            elif choice == 4:
                clear_batch_item()
                break
            elif choice == 5:
                clearScreen()
                main()
                break
        except ValueError:
            print(Fore.RED + "Invalid input. Enter number for menu choice.\n")
            time.sleep(1)
            continue


def check_batch():
    """
    Pull batch data from batch google sheet and allow
    user to update quantity and amend worksheet
    """
    typePrint("Fetching batch numbers for today...")
    time.sleep(1.5)
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + "** TODAYS BATCH NUMBERS **\n")
    batch_sheet = SHEET.worksheet("batch")
    batch_list = batch_sheet.col_values(1)
    q_list = batch_sheet.col_values(2)
    # list/zip for parallel iteration
    pairs = list(zip(batch_list, q_list))
    for pair in pairs:
        print(Fore.CYAN + '- ', pair[0], Fore.CYAN + ': ', pair[1])
    print("\n")
    print(Fore.YELLOW + "Thank you very much for your Service.\n")
    while True:
        user_input = input("Would you like to update batches? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            print("\n")
            batch_options()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()
            break
    time.sleep(1)
    return_main()


def return_invt_menu():
    """
    Print updated inventory data for user and
    provide input choices
    """
    invt_sheet = SHEET.worksheet("inventory")
    invt_list = invt_sheet.col_values(1)
    ing_list = invt_sheet.col_values(2)
    pairs = list(zip(invt_list, ing_list))
    for pair in pairs:
        print(Fore.CYAN + '- ', pair[0], Fore.CYAN + ': ', pair[1])
    print("\n")
    while True:
        user_input = input("Update inventory? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            print("\n")
            invt_options()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()
            break


def add_item():
    """
    Add new items to inventory and update google sheet
    """
    invt_sheet = SHEET.worksheet("inventory")
    new_ing = input("Enter a new item to add to the"
                    " inventory: \n")
    new_ing_v = input("Enter new item quantity"
                      " (numerical value only): \n")
    invt_sheet.append_row([new_ing, new_ing_v])
    print(Fore.GREEN + "Inventory successfully updated.\n")
    return_invt_menu()


def user_update_ing():
    """
    Allow user input to update inventory levels
    """
    invt_sheet = SHEET.worksheet("inventory")
    records = invt_sheet.get_all_records()
    while True:
        ing_c = input("Enter item name as displayed"
                      " above: \n")
        record_found = False
        for record in records:
            if record["Souvenirs"] == ing_c:
                record_found = True
                while True:
                    try:
                        update_q = int(input(f"Enter value for {ing_c}:\n"))
                        record["Quantity"] = update_q
                        # update with new data to inventory sheet
                        for i, record in enumerate(records, start=2):
                            invt_sheet.update_cell(i, 2, record["Quantity"])
                        print(Fore.GREEN + "Inventory successfully updated.\n")
                        cho = input("Update another item? Enter Y or N.")
                        print("\n")
                        if cho == 'Y' or cho == 'y':
                            clearScreen()
                            print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT +
                                  "*** CURRENT INVENTORY LEVELS ***\n")
                            time.sleep(.5)
                            return_invt_menu()
                        elif cho == 'N' or cho == 'n':
                            return_main()
                        else:
                            print(Fore.RED + "Invalid input.\n")
                            check_invt()
                    except ValueError:
                        print(Fore.RED + "Value must be numerical.\n")
                        continue
        if not record_found:
            print(Fore.RED + "Item not found in inventory.\n")
            continue


def change_invt_item():
    """
    Change item in inventory.
    """
    invt_sheet = SHEET.worksheet("inventory")
    ing_o = input("Enter item name as displayed"
                  " above: \n")
    ing_n = input("Enter the new item: \n")
    values = invt_sheet.col_values(1)
    for i, value in enumerate(values):
        if value == ing_o:
            invt_sheet.update_cell(i+1, 1, ing_n)
    print(Fore.GREEN + "Inventory successfully updated.\n")
    return_invt_menu()


def clear_invt_item():
    """
    Clear inventory item completely from records
    """
    invt_sheet = SHEET.worksheet("inventory")
    ing_del = input("Enter item name as displayed"
                    " above: \n")
    cells_needed = invt_sheet.findall(ing_del, in_column=1)
    rows_to_clear = [cell.row for cell in cells_needed]
    for row in rows_to_clear:
        invt_sheet.delete_rows(row)
    print(Fore.GREEN + "Records updated successfully.\n")
    return_batch_menu()


def invt_options():
    """
    Menu to choose between adding items, changing items name
    or updating quantity.
    """
    print(Back.MAGENTA + Fore.WHITE + "*** INVENTORY MENU ***")
    print("\n")
    print(Fore.CYAN + "1. Add new item\n")
    print(Fore.CYAN + "2. Change item\n")
    print(Fore.CYAN + "3. Update item quantity\n")
    print(Fore.CYAN + "4. Clear item\n")
    print(Fore.CYAN + "5. Return to main menu\n")
    while True:
        try:
            choice = int(input("Please choose from the menu: \n"))
            if choice == 1:
                add_item()
                break
            elif choice == 2:
                change_invt_item()
                break
            elif choice == 3:
                user_update_ing()
                break
            elif choice == 4:
                clear_invt_item()
                break
            elif choice == 5:
                clearScreen()
                main()
                break
        except ValueError:
            print(Fore.RED + "Invalid input. Enter number for menu choice.\n")
            time.sleep(1)
            continue


def check_invt():
    """
    Pull inventory data from inventory google sheet and allow
    user to update levels and amend worksheet
    """
    typePrint("Checking inventory levels...")
    time.sleep(1)
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + "*** CURRENT INVENTORY LEVELS ***\n")
    invt_sheet = SHEET.worksheet("inventory")
    ing_list = invt_sheet.col_values(1)
    q_list = invt_sheet.col_values(2)
    # list/zip for parallel iteration
    pairs = list(zip(ing_list, q_list))
    for pair in pairs:
        print(Fore.CYAN + '- ', pair[0], Fore.CYAN + ': ', pair[1])
    print("\n")
    while True:
        try:
            u_input = input("Would you like to update an item? Enter Y or N\n")
            if u_input == 'Y' or u_input == 'y':
                invt_options()
                break
            elif u_input == 'N' or u_input == 'n':
                return_main()
                break
        except ValueError:
            print(Fore.RED + "Value must be numerical.\n")
            continue
    time.sleep(1)
    return_main()


def exit():
    """
    return to program start screen
    """
    typePrint("Thank you for your service.\n")
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
    print(Back.MAGENTA + Fore.WHITE + "*** Welcome to Afro GiftShop ***\n")
    time.sleep(1)
    typePrint("Please choose from the menu below.\n")
    time.sleep(1)
    print(Fore.CYAN + "1. Sales menu\n")
    print(Fore.CYAN + "2. Shop Batch\n")
    print(Fore.CYAN + "3. Shop inventory\n")
    print(Fore.CYAN + "4. Exit\n")
    while True:
        try:
            choice = int(typeInput("Please enter your choice: \n"))
            if choice == 1:
                day_sales()
                break
            elif choice == 2:
                check_batch()
                break
            elif choice == 3:
                check_invt()
                break
            elif choice == 4:
                exit()
                break
        except ValueError:
            print(Fore.RED + "Invalid input. Enter number for menu choice.\n")
            time.sleep(1)
            continue


prog_start()
main()
