# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# Further Exploration
# Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

start_num = int(input('Starting number? '))
end_num = int(input('Ending number? '))

for number in range(start_num, end_num + 1, 2):
    if number % 2 != 0:             # odd number
        print(number)
    else:                           # even number
        number += 1
        if number <= end_num:
            print(number)