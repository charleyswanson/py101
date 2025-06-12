# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

def add(num):
    beginning_number = 0
    for i in range(1, (num + 1)):
        beginning_number += i
    return beginning_number

def product(num):
    beginning_number = 1
    for i in range(1, (num + 1)):
        beginning_number *= i
    return beginning_number

user_number = int(input('Please enter an integer greater than 0: '))
sum_or_product = input('Enter "s" to compute the sum, or "p" to compute the product. ')

print()

if sum_or_product == 's':
    print(f"The sum of the integers between 1 and {user_number} is "
          f"{add(user_number)}.")

elif sum_or_product == 'p':
    print(f"The product of the integers between 1 and {user_number} is "
          f"{product(user_number)}.")

else:
    print("Sorry, that wasn't a valid entry.")

