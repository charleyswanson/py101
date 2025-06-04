# For a challenging but fun exercise, try word wrapping messages that are too long to fit, so that they appear on multiple lines but are still contained within the box. This isn't an easy problem, but it's doable with basic Python.

def print_in_box(str, box_width = float('inf')):
    if box_width < len(str):                        # box is narrower than str
        horiz_line = f"+{'-' * (box_width - 2)}+"
        blank_line = f"|{' ' * (box_width - 2)}|"
        print(horiz_line)
        print(blank_line)

# -----------------------------------------

        word_list = str.split()
        line_to_print = '|'
        index = 0

        while index < len(word_list) - 1:
            
            # assemble a line to print, as long as it's not the last word
            while len(line_to_print) + len(word_list[index]) < box_width - 2:
                if index < len(word_list) - 1:
                    word = word_list[index]
                    line_to_print = line_to_print + ' ' + word
                    index += 1
                else:
                    break
            
            # handling the last word in the list; one line or two
            if index == len(word_list) - 1:
                word = word_list[index]
                if len(line_to_print) + len(word_list[index]) < box_width - 2:
                    extra_spaces = box_width - len(f'{line_to_print} {word} +')
                    print(f'{line_to_print} {word} {extra_spaces * ' '}|')
                else:
                    extra_spaces = box_width - len(f'{line_to_print} |')
                    print(f'{line_to_print} {extra_spaces * ' '}|')
                    extra_spaces = box_width - len(f'| {word} |')
                    print(f'| {word} {extra_spaces * ' '}|')
            
            # print the assembled line
            else:
                extra_spaces = box_width - len(f'{line_to_print} |')
                print(f'{line_to_print} {extra_spaces * ' '}|')
            line_to_print = '|'

# -----------------------------------------

        print(blank_line)
        print(horiz_line)

    else:                                           # box is wider than str
        horiz_line = f"+{'-' * (len(str) + 2)}+"
        blank_line = f"|{' ' * (len(str) + 2)}|"

        print(horiz_line)
        print(blank_line)
        print(f"| {str} |")
        print(blank_line)
        print(horiz_line)

print_in_box('To boldly go where no one has gone before. Really, ever.', 28)
# print_in_box('T o b o l wd xhdswy gxxxxxxx o w h e r e n o o n e h a s g o n , e v e r.', 25)