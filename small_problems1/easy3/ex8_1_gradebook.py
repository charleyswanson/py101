# Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

# Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'

# Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.

def get_grade(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    match average:
        case x if x >= 90:
            return 'A'
        case x if 80 <= x < 80:
            return 'B'
        case x if 70 <= x < 80:
            return 'C'
        case x if 60 <= x < 70:
            return 'D'
        case _:
            return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True