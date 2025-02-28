# For a challenging but fun exercise, try word wrapping messages that are too long to fit, so that they appear on multiple lines but are still contained within the box. This isn't an easy problem, but it's doable with basic Python.

def print_in_box(str, box_width = float('inf')):
    if box_width < len(str):                        # box is narrower than str
        horiz_line = f"+{'-' * (box_width - 2)}+"
        blank_line = f"|{' ' * (box_width - 2)}|"
        print(horiz_line)
        print(blank_line)

# -----------------------------------------

        word_list = str.split()
        current_line = ' ' + word_list.pop(0)
        while len(word_list) > 0:
            current_word = word_list[0]
            while len(current_line + ' ' + current_word) < box_width - 4 and word_list:
                current_word = word_list.pop(0)
                current_line = current_line + ' ' + current_word
            print(f'|{current_line} |')
            current_line = ''
        
        print(blank_line)
        print(horiz_line)

# -----------------------------------------

    else:                                           # box is wider than str
        horiz_line = f"+{'-' * (len(str) + 2)}+"
        blank_line = f"|{' ' * (len(str) + 2)}|"

        print(horiz_line)
        print(blank_line)
        print(f"| {str} |")
        print(blank_line)
        print(horiz_line)

print_in_box('To boldly go where no one has gone before. Really, ever.', 20)
# print_in_box('T o b o l wd xhwy gxxxxxxx o w h e r e n o o n e h a s g o n , e v e r.', 20)