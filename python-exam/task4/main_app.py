from is_palindrome_check import is_palindrome
# --- Main Program Logic ---

if __name__ == "__main__":
   print("\n" + "*" * 28)
   print("---   PALINDROME CHECK  ---")
   print("    write 'quit' to exit")
   print("*" * 28 + "\n")

   while True:
       # prompt user to input a string
    user_string = input("Enter a string to check if it is a palindrome: ")

    # quit-option
    if user_string.lower() == 'quit': 
       print("Exiting program. Goodbye!")
       break

    # call function to determine if the entered string is a palindrome
    if is_palindrome(user_string):
        # display the result with output message
        print(f"The string '{user_string}' is a palindrome.")
    else:
        print(f"The string '{user_string}' is not a palindrome.")

    print("-" * 40 + "\n")

    
