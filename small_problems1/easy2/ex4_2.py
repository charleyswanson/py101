# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

# Further Exploration

# Suppose we want to generalize this function to a "power to the n" type function: cubed, to the 4th power, to the 5th, etc. How would we go about doing so while still using the multiply function?

def multiply(num1, num2):
    return num1 * num2

user_number = int(input('What number? '))
user_power = int(input('To what power? '))

answer = 1
for i in range(user_power):
    answer = multiply(answer, user_number)
print(answer)