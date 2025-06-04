# Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

def crunch(str):
    if str == '':                           # check for empty string
        return str
    else:
        answer = str[0]                     # grab the first letter
        for i in range(1,len(str)):         # cycle letters, starting at 2nd one
            if str[i] != answer[-1]:        # current letter == last in answer?
                answer += str[i]            # if no, concat letter to answer
    return(answer)

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')