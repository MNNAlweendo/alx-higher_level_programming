#!/usr/bin/python3
def text_indentation(text):
    """
    Print the text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Iterate through the characters in the text
    for char in text:
        # Print the character
        print(char, end='')

        # If the character is '.', '?', or ':', print two new lines
        if char in ['.', '?', ':']:
            print("\n\n", end='')

    # Print a new line at the end
    print()

