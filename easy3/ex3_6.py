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
        word = word_list[0]

        while index < len(word_list) - 1:
            while len(line_to_print) + len(word) < box_width - 2:
                line_to_print = line_to_print + ' ' + word
                # print(f'{line_to_print}')
                index += 1
                word = word_list[index]
                # print(f'                index: {index} / word: {word}')
            print(f'{line_to_print} !')

            if index < len(word_list) - 1:
                line_to_print = "| " + word
                index += 1
                # print(index)
                word = word_list[index]
                # print(f'                INDEX: {index} / WORD: {word}')
            
        line_to_print = line_to_print + ' ' + word
        print(index)

        if index != len(word_list) - 1:
            if len(line_to_print) < box_width - 2:
                print(f'{line_to_print} |')
            else:
                end_list = line_to_print.split()
                last_word = end_list.pop()
                print(' '.join(end_list))
                print(f'| {last_word} |')

# To boldly go where no one has gone before. Really, ever.
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

# print_in_box('To boldly go. Really, ever.', 20)

print_in_box('To boldly go where no one has gone before. Really, ever.', 30)
# print_in_box('T o b o l wd xhwy gxxxxxxx o w h e r e n o o n e h a s g o n , e v e r.', 20)