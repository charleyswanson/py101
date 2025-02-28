# Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

def crunch(str):
    index = 0
    answer = ''

    while index < len(str):
        if index == len(str) - 1 or str[index] != str[index + 1]:
            answer += str[index]
        index += 1
    
    return answer


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')