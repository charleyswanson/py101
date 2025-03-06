# Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).

def clean_up(str): 
    final_str = ''

    for letter in str:
        if letter.isalpha():
            final_str += letter
        elif len(final_str) == 0 or final_str[-1] != ' ':
            final_str += ' '
    
    return final_str

print(clean_up("---whhat's my +*& line?") == " whhat s my line ")
# True