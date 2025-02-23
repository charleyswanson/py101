# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

bill = float(input('What is the bill? '))
tip = float(input('What is the tip percentage? ')) / 100

tip_amount = bill * tip
total_bill = bill + tip_amount

print()
print(f'The tip is ${tip_amount:.2f}')
print(f'The total is ${total_bill:.2f}')