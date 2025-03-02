# this never worked :/

def print_in_box(str, box_width = float('inf')):
    if box_width < len(str):                        # box is narrower than str
        horiz_line = f"+{'-' * (box_width - 2)}+"
        blank_line = f"|{' ' * (box_width - 2)}|"
        print(horiz_line)
        # print(blank_line)

# -----------------------------------------

        word_list = str.split()
        current_line = ' ' + word_list.pop(0)
        while len(word_list) > 0:
            current_word = word_list[0]
            while len(current_line + ' ' + current_word) < box_width - 4:

                print(f'   {len(current_line + ' ' + current_word)}')
                print(f'   {word_list}')
                print(f'   {current_word}')

                current_word = word_list.pop(0)
                current_line = current_line + ' ' + current_word

                print(f'   {len(current_line + ' ' + current_word)}')
                print(f'   |{current_line} |')
                print()

                if not word_list:
                    break

            print(f'|{current_line} |')

            current_line = ''
        
        # print(blank_line)
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

# print_in_box('To boldly go. Really, ever.', 20)

print_in_box('To boldly go where no one has gone before. Really, ever.', 20)
# print_in_box('T o b o l wd xhwy gxxxxxxx o w h e r e n o o n e h a s g o n , e v e r.', 20)