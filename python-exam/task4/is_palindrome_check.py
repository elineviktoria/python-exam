# --- Palindrome Checking Function ---
def is_palindrome(text_input):
    """
    Checks if a given string is a palinfrome.
    The check is case-insensitive and ignores spaces and punctuation.
    - args: text_input (str): the string to check
    - returns: bool - true, if the string is a palindrome, false otherwise
    """

    # preprocessing the string
    processed_string = text_input.lower()

    # remove non-alphanumeric characters - build string containing only letters and numbers
    cleaned_string = ""

    # loop through each character
    for char in processed_string:
        # check if character is alphanumeric
        if char.isalnum(): # L3
            cleaned_string += char # string concatenation
        
    # Palindrome check
    left_index = 0
    right_index = len(cleaned_string) - 1

    while left_index < right_index:
        if cleaned_string[left_index] != cleaned_string[right_index]:
            return False # characters dont match
        left_index += 1
        right_index -= 1
    return True # all characters match