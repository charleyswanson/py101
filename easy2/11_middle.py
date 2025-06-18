# Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should return exactly one character. If the string has an even length, you should return exactly two characters.

def center_of(str_):
    length = len(str_)
    print(length)
    if length % 2 == 0:
        starting_letter = (int(length / 2) - 1)
        print(str_[starting_letter: (starting_letter + 1)])

print(center_of('I Love Python!!!'))
print(center_of('Launch School'))
print(center_of('Launchschool'))
print(center_of('Launch'))
print(center_of('Launch School is #1'))
print(center_of('x'))

# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True