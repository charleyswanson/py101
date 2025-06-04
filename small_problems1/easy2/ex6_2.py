# Further Exploration
# Our solution ignored two edge cases since we explicitly stated that you didn't have to handle them: strings that contain no words or just one word.

# Suppose we need a function that retrieves the middle word of a phrase/sentence. What edge cases need to be considered? How would you handle those edge cases without ignoring them? Write a function that returns the middle word of a phrase or sentence. It should handle all of the edge cases you thought of.

# 0 words
# 1 word
# even number of words

def middle_word(str):
    word_list = str.split()
    if len(word_list) == 0:                     # empty string
        return 'Need something to work with here!'
    elif len(word_list) % 2 != 0:               # odd number of words
        return word_list[len(word_list) // 2]
    else:                                       # even number, round down
        return word_list[ (len(word_list) // 2) - 1 ]

# These examples should print True
print(middle_word("") == "Need something to work with here!")
print(middle_word("word") == "word")
print(middle_word("One two words") == "two")
print(middle_word("Launch School is great!") == "School")
print(middle_word("Never half-ass two things. Whole-ass one thing."))