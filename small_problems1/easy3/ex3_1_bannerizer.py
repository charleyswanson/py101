# Write a function that takes a short line of text and prints it within a box.

def print_in_box(str):
    boxed_str = '| ' + str + ' |'
    dashes_or_spaces = len(boxed_str) - 2
    print('+' + ('-' * dashes_or_spaces) + '+')
    print('|' + (' ' * dashes_or_spaces) + '|')
    print(boxed_str)
    print('|' + (' ' * dashes_or_spaces) + '|')
    print('+' + ('-' * dashes_or_spaces) + '+')

print_in_box('To boldly go where no one has gone before.')
print()
print_in_box('')

# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+