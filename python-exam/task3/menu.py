# --- Menu Class Implementation ---
class Menu:
    """
    Managed the display og menu options and gets user input
    - attribute: options (a list of strings)
    """

    def __init__(self):
        # constructor for the Menu class - initializes an empty list for menu options
        self.options = [] # data structure: list

    def add_option(self, option_text):
        # add a menu option to the list of options
        self.options.append(option_text) 

    def get_input(self):
        # displays all menu option and prompts the user for their choice - validates the input as int and withing the valid range of options
        if not self.options:
            print("Menu has no options to display.")
            return -1 # indicates no option / error
        
        print("\n" + "*" * 20 + "\n")
        print("---  BANK MENU   ---")
        print("\n" + "*" * 20 + "\n")
        # loop to display options
        for i in range(len(self.options)):
            print(f"{i + 1} {self.options[i]}") # displays options starting from 1
        print("*" * 20)
        
        while True:
            try:
                choice_str = input(f"Enter your choice (1-{len(self.options)}): ")
                choice_int = int(choice_str) # contert string to int

                # conditional check
                if 1 <= choice_int <= len(self.options):
                    return choice_int # valid choice
                else:
                    print(f"Invalid choice. Please enter a number between 1 and {len(self.options)}.")
            except ValueError: # handles non-integer input
                print("Invalid input. Please enter a number.")
                