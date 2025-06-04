# Write a function that takes a short line of text and prints it within a box.

def print_in_box(str):
    horiz_line = f"+{'-' * (len(str) + 2)}+"
    blank_line = f"|{' ' * (len(str) + 2)}|"

    print(horiz_line)
    print(blank_line)
    print(f"| {str} |")
    print(blank_line)
    print(horiz_line)

print_in_box('To boldly go where no one has gone before.')
print()
print_in_box('')

# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+