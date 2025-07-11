# --- Main Application Logic ---
from bank_account import BankAccount
from menu import Menu

# help function
def get_validated_float_input(prompt_message):
    # gets and validates float input from the user
    while True:
        try:
            value_str = input(prompt_message)
            value_float = float(value_str)
            return value_float
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    # create menu object and add options
    main_menu = Menu()
    main_menu.add_option("Open a new account")
    main_menu.add_option("Deposit money into your account")
    main_menu.add_option("Withdraw money from your account")
    main_menu.add_option("Add interest to your account")
    main_menu.add_option("Get the current balance of your account")
    main_menu.add_option("Quit")

    current_account = None # variable to hold the BankAccount object, initially no account exists
    print("Welcome to the Bank Account Manager System!")

    # main program loop
    while True:
        user_choice = main_menu.get_input()
        print("\n" * 2)

        # conditional processing of menu choices
        match user_choice:
            case 1: # open a new account
                print("--- Option 1: Open a new account ---")
                if current_account is not None:
                    print("Account is already open.")
                else:
                    initial_deposit = get_validated_float_input("Enter initial deposit amount (e.g. 100): ")
                    if initial_deposit < 0:
                        print("Initial deposit cannot be negative. Account created with 0.0 balance.")
                        current_account = BankAccount(0.0)
                    else:
                        current_account = BankAccount(initial_deposit) # create BankAccount object
                        print("New account opened successfully.")
                    print(current_account) # uses BankAccount.__str__
                    # except ValueError:
                    #     print("Invalid amount entered. Account creation failed. Please enter a number.")
                # print("-" * 40)
        
            case 2: # deposit
                print("--- Option 2: Deposit money ---")
                if current_account is None:
                    print("No account open. Please open an account first (option 1).")
                else:
                    deposit_amount = get_validated_float_input("Enter amount to deposit: ")
                    current_account.deposit(deposit_amount)
                # print("-" * 40)

            case 3: # withdraw
                print("--- Option 3: Withdraw money ---")
                if current_account is None:
                    print("No account open. Please open an account first (option 1).")
                else:
                    withdraw_amount = get_validated_float_input("Enter amount to withdraw: ")
                    current_account.withdraw(withdraw_amount)
                # print("-" * 40)

            case 4: # add interest
                print("--- Option 4: Add interest ---")
                if current_account is None:
                    print("No account open. Please open an account first (option 1).")
                else:
                    rate_percentage = get_validated_float_input("Enter interest rate as a percentage (e.r. 5 for 5%): ")
                    if rate_percentage < 0:
                        print("Interest rate cannot be negative.")
                    else:
                        decimal_rate = rate_percentage / 100.0
                        current_account.add_interest(decimal_rate)
                # print("-" * 40)

            case 5: # get balance
                print("--- Option 5: Get current balance ---")
                if current_account is None:
                    print("No account open. Please open an account first (option 1).")
                else:
                    print(current_account)
                # print("-" * 40)
            
            case 6: # quit
                print("Thank you for using the Bank Account Management System. Goodbye!")
                break # exit while loop, terminating program

            case -1: # error from menu
                print("Menu error. Exiting.")
                break
        
        if not (user_choice == 6 or user_choice == -1): # don't print seperator if quitting the program
            print("-" * 40)


        # GAMMEL KODE UTEN MATCH-CASE
        # if user_choice == 1: # open a new account
        #     print("--- Option 1: Open a new account ---")
        #     if current_account is not None:
        #         print("Account is already open.")
        #     else:
        #         try:
        #             initial_deposit_str = input("Enter initial deposit amount (e.g., 100.00): ")
        #             initial_deposit = float(initial_deposit_str) # convert to float
        #             if initial_deposit < 0:
        #                 print("Initial deposit cannot be negative. Account created with 0.0 balance.")
        #                 current_account = BankAccount(0.0)
        #             else:
        #                 current_account = BankAccount(initial_deposit) # create BankAccount object
        #                 print("New account opened successfully.")
        #                 print(current_account) # uses BankAccount.__str__
        #         except ValueError:
        #             print("Invalid amount entered. Account creation failed. Please enter a number.")
        #     print("-" * 40)
        
        # elif user_choice == 2: # deposit
        #     print("--- Option 2: Deposit money ---")
        #     if current_account is None:
        #         print("No account open. Please open an account first (option 1).")
        #     else:
        #         try:
        #             deposit_amount_str = input("Enter amount to deposit: ")
        #             deposit_amount = float(deposit_amount_str)
        #             current_account.deposit(deposit_amount)
        #         except ValueError:
        #             print("Invalid amount. Please enter a number.")
        #     print("-" * 40)

        # elif user_choice == 3: # withdraw
        #     print("--- Option 3: Withdraw money ---")
        #     if current_account is None:
        #         print("No account open. Please open an account first (option 1).")
        #     else:
        #         try:
        #             withdraw_amount_str = input("Enter amount to withdraw: ")
        #             withdraw_amount = float(withdraw_amount_str)
        #             current_account.withdraw(withdraw_amount)
        #         except ValueError:
        #             print("Invalid amount. Please enter a number.")
        #     print("-" * 40)

        # elif user_choice == 4: # add interest
        #     print("--- Option 4: Add interest ---")
        #     if current_account is None:
        #         print("No account open. Please open an account first (option 1).")
        #     else:
        #         try:
        #             # asking user for rate as percentage
        #             rate_str = input("Enter interest rate as a percentage (e.g., 5 for 5%): ")
        #             rate_percentage = float(rate_str)
        #             if rate_percentage < 0:
        #                 print("Interest rate cannot be negative.")
        #             else:
        #                 decimal_rate = rate_percentage / 100.0 # convert percentage to decimal
        #                 current_account.add_interest(decimal_rate)
        #         except ValueError:
        #             print("Invalid rate. Please enter a number for the percentage")
        #     print("-" * 40)

        # elif user_choice == 5: # get balance
        #     print("--- Option 5: Get current balance ---")
        #     if current_account is None:
        #         print("No account open. Please open an account first (option 1).")
        #     else:
        #         print(current_account)
        #     print("-" * 40)
        
        # elif user_choice == 6: # quit
        #     print("Thank you for using the Bank Account Management System. Goodbye!")
        #     break # exit while loop, terminating program

        # elif user_choice == -1: # error from menu
        #     print("Menu error. Exiting.")
        #     break