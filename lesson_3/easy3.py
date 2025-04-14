# 1
# Write two different ways to remove all of the elements from the following list:

# numbers = [1, 2, 3, 4]
# print(numbers)
# numbers = []
# numbers.clear()
# while numbers:
#     numbers.pop()
# print(numbers)

# 5
# The following function unnecessarily uses two return statements to return boolean values. Can you rewrite this function so it only has one return statement and does not explicitly use either True or False?
# Try to come up with two different solutions.

# def is_color_valid(color):
#     if color == "blue" or color == "green":
#         return True
#     else:
#         return False

def is_color_valid(color):
    # return color == "blue" or color == "green"
    return color in ["blue", "green"]

print(is_color_valid("red"))