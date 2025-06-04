# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

def is_odd(number):
    return number % 2 != 0

my_int = int(input("How about a number? "))

print(f"Is {my_int} odd? -> {is_odd(my_int)}")