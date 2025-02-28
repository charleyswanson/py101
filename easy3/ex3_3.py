# Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided as a second argument (the width is the width of the box itself). You may assume no maximum if the second argument is omitted.

def print_in_box(str, box_width = float('inf')):
    if box_width < len(str):
        str = str[0 : box_width - 4]
        horiz_line = f"+{'-' * (box_width - 2)}+"
        blank_line = f"|{' ' * (box_width - 2)}|"
    else:
        horiz_line = f"+{'-' * (len(str) + 2)}+"
        blank_line = f"|{' ' * (len(str) + 2)}|"

    print(horiz_line)
    print(blank_line)
    print(f"| {str} |")
    print(blank_line)
    print(horiz_line)

print_in_box('To boldly go where no one has gone before.', 25)