# this never worked :/

# def print_in_box(str, box_width = float('inf')):
#     print(len(str))
#     print((len(str) // box_width) + 1)
#     if box_width < len(str):                        # box is narrower than str
#         horiz_line = f"+{'-' * (box_width - 2)}+"
#         blank_line = f"|{' ' * (box_width - 2)}|"
#         print(horiz_line)
#         print(blank_line)

#         lines = (len(str) // box_width) + 2
#         start_index = 0
#         end_index = box_width - 4
#         while lines > 0:
#             current_line = str[start_index : end_index].strip()
#             extra_spaces = box_width - len(current_line) - 4
#             print(f'| {current_line}{" " * extra_spaces} |')
#             start_index += box_width - 4
#             end_index += box_width - 4
#             lines -= 1
        
#         print(blank_line)
#         print(horiz_line)

#     else:                                           # box is wider than str
#         horiz_line = f"+{'-' * (len(str) + 2)}+"
#         blank_line = f"|{' ' * (len(str) + 2)}|"

#         print(horiz_line)
#         print(blank_line)
#         print(f"| {str} |")
#         print(blank_line)
#         print(horiz_line)

# print_in_box('To boldly go where no one has gone before. Really, ever.')