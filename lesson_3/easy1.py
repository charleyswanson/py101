# 2
# str1 = "What's up, Doc?"
# print(str1.endswith("!"))

# 3
# Show two different ways to create a new string with "Four score and " prepended to the front of the string referenced by famous_words.

# famous_words = "seven years ago..."
# all_words = "Four score and " + famous_words
# all_words = f'Four score and {famous_words}'
# print(all_words)

# 4
# munsters_description = "the Munsters are CREEPY and Spooky."
# print(munsters_description.capitalize())

# 5
# munsters_description = "The Munsters are creepy and spooky."
# print(munsters_description.swapcase())

# 6
# str1 = "Few things in life are important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."
# print("Dino" in str1)
# print("Dino" in str2)

# 7
# How can we add the family pet, "Dino", to the following list?
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# print(flintstones)

# 8
# How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? Replace the call to append with another method invocation.
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# new_members = ["Dino", "Hoppy"]
# flintstones.extend(new_members)
# print(flintstones)

# 9
# Print a new version of the sentence given by advice that ends just before the word house. Don't worry about spaces or punctuation: remove everything starting from the beginning of house to the end of the sentence.
# Expected output:
# Few things in life are as important as

# advice = "Few things in life are as important as house training your pet dinosaur."
# new_advice = advice.split("house")[0]
# print(new_advice)

# 10
# Print the following string with the word important replaced by urgent:

advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace("important", "urgent"))
