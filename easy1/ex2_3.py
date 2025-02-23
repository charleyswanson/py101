# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# Further Exploration
# Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

start_num = int(input('Starting number? '))
end_num = int(input('Ending number? '))

counter = start_num

while counter <= end_num:
    if counter % 2 != 0:
        print(counter)
    else:
        counter += 1
        print(counter)
    counter += 2