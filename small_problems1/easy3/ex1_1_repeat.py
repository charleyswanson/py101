# Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

def repeat(word, repeat):
    for i in range(repeat):
        print(word)

repeat('Hello', 3)