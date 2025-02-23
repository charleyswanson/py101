# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

def sum(num):
    answer = 0
    for i in range(1, num + 1):
        answer += i
    return answer

def product(num):
    answer = 1
    for i in range(1, num + 1):
        answer *= i
    return answer

number = int(input('Please enter an integer greater than 0: '))
math = input('Enter "s" to compute the sum, or "p" to compute the product. ')

if math == 's':
    print()
    print(f'The sum of the integers between 1 and {number} '
          f'is {sum(number)}.')
elif math == 'p':
    print()
    print(f'The product of the integers between 1 and {number} '
          f'is {product(number)}.')
else:
    print()
    print("Sorry, needed an 's' or a 'p' for this to work out.")