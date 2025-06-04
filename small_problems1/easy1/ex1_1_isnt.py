# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

def is_it_odd(number):
    return number % 2 != 0

test_num = abs(int(input('How about a number? ')))
print(f'Is {test_num} odd? -> {is_it_odd(test_num)}')